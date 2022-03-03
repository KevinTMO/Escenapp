from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '73be4410e3006053dfe913a29efe79be'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


''' Below SQLite configs '''

class User(db.Model):
    '''
    litedb to store user info
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    profile = db.relationship('Artist', backref='artist', lazy=True)

    def __repr__(self):
        """
        return a repr string of User object
        """
        return (f'User("{self.name}", "{self.email}")')


class Artist(db.Model):
    """
    ltedb to store artist info
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    instrument = db.Column(db.String(50), nullable=False)
    biography = db.Column(db.String(150), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    usr_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
        return repr string of Artist obj
        """
        return ('{}, {}, {}, {}'.format(self.name, self.genre, self.instrument,
                                        self.biography))


''' Below route methods '''

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
