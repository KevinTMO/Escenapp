# from datetime import datetime
# from flask_sqlalchemy import SQLALCHEMY_DATABASE_URL
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '73be4410e3006053dfe913a29efe79be'
# APP.CONFIG['SQLALCHEMY_DATABASE_URL'] = ''
# db = SQLAlchemy(app)


'''Below route methods '''

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


''' Below flask ip/port config '''


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
