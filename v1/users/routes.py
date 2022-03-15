from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from v1.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                      RequestResetForm, ResetPasswordForm, UpdateEmailForm)
from v1.models import Artist, PostEvent
from v1 import app, db, bcrypt, mail
from v1.users.utils import save_picture, send_reset_email


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    """
    artist registration form
    """
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        artist = Artist(name=form.name.data, email=form.email.data, password=hashed_password,
                        genre=str(form.genre.data), instrument=str(form.instrument.data))
        db.session.add(artist)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    def login for redirection test after registration of usr
    """
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))

    form = LoginForm()

    if form.validate_on_submit():
        artist = Artist.query.filter_by(email=form.email.data).first()
        if artist and bcrypt.check_password_hash(artist.password, form.password.data):
            login_user(artist, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """
    User account route
    """
    form = UpdateAccountForm()
    formE = UpdateEmailForm()
    events = PostEvent.query.all() # get all events from db
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        if formE.email.data:
            current_user.email = formE.email.data
        if form.biography.data:
            current_user.biography = form.biography.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('users.account'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file,
                           form=form, formE=formE, events=events)


@users.route('/logout')
def logout():
    """
    def to logout the user from his account
    """
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))

    form = RequestResetForm()
    if form.validate_on_submit():
        artist = Artist.query.filter_by(email=form.email.data).first()
        send_reset_email(artist)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))

    artist = Artist.verify_reset_token(token)
    if artist is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        artist.password = hashed_password
        db.session.commit()
        flash(f'Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))

    return render_template('reset_token.html', title='Reset Password', form=form)
