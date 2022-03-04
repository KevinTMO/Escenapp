from flask import render_template, url_for, flash, redirect
from v1.forms import RegistrationForm, LoginForm
from v1.models import User, Artist
from v1 import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    def landing page route using only domain or route in browser
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for { form.name.data }!', 'success')
        return redirect(url_for('login'))
    return render_template('home.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    def login for redirection test after registration of usr
    """
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "admin@artist.com" and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
