from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '9ad4d2f8fdaaac12aa160ef91df5ed9b'


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

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = RegistrationForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            flash(f'Account created for {form.name.data}!', 'success')
            return redirect(url_for('login'))
    return render_template('home.html', form=form)


'''
@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
'''

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
