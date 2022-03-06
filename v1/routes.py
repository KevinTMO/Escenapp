from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, login_required, current_user
from v1.forms import RegistrationForm, LoginForm, UpdateAccountForm
from v1.models import Artist
from v1 import app, db, bcrypt
from PIL import Image
import secrets
import os

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    def landing page route using only domain or route in browser
    """
    return render_template('home.html', title='Home')



@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    artist registration form
    """
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        artist = Artist(name=form.name.data, email=form.email.data, password=hashed_password,
                        genre=str(form.genre.data), instrument=str(form.instrument.data))
        db.session.add(artist)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    def login for redirection test after registration of usr
    """
    if current_user.is_authenticated:
        return redirect(url_for('account'))

    form = LoginForm()

    if form.validate_on_submit():
        artist = Artist.query.filter_by(email=form.email.data).first()
        if artist and bcrypt.check_password_hash(artist.password, form.password.data):
            login_user(artist, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('account'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


def save_picture(form_picture):
    """
    function should save a picture in a dir by secret token hex
    """
    random_hex = secrets.token_hex(8)
    _, fileExt = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + fileExt
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)


    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)

    img.save(picture_path)

    return picture_fn

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """
    User account route
    """
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.email = form.email.data
        current_user.biography = form.biography.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file,
                           form=form)


@app.route('/logout')
def logout():
    """
    def to logout the user from his account
    """
    logout_user()
    return redirect(url_for('login'))
