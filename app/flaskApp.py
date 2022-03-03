from flask import Flask, render_template, url_for, flash, redirect, request
from datetime import datetime
from flask_sqlalchemy import SQLALCHEMY_DATABASE_URL
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '9ad4d2f8fdaaac12aa160ef91df5ed9b'
APP.CONFIG['SQLALCHEMY_DATABASE_URL'] = ''
db = SQLALlchemy(app)

'''
forms = [
    {
        'name': 'Sergio',
        'email': 'sergiovera@whatever.com',
        'password': 'funkified',
        'confirm': 'funkified'
    },

    {
        'name': 'Yared',
        'email': 'yaredtorres@whatever.com',
        'password': 'partychu',
        'confirm': 'partychu'
    }
]

numbers = [
    {
        'nmbr': [1, 2]
    }
]
'''

def __repr__(self):
    '''
    Return a reprs string of objects
    '''
    return f"Post('{self.title}', '{self.date_posted}')"


@app.route('/')
@app.route('/home')
def home():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'Account created for {form.name.data}!', 'success')
            return redirect(url_for('login'))
    return render_template('home.html', form=form)


'''
Not in use at the moment. For testing purposes.

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
'''

# Using this route just for redirection test
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


"""
For Ilustration Purposes-->
----------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return "User'{}', '{}', '{}')".format(self.username, self.email), self.image_file)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'sergiovera@whatever.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
"""

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
