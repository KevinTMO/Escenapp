from v1 import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """
    this function should work the process of login/logout of the user
    by id
    """
    return User.query.get(int(user_id))

""" Below is the classes/attrs for the db  """

class User(db.Model, UserMixin):
    '''
    litedb to store user info
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
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
    usr_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """
        return repr string of Artist obj
        """
        return ('{}, {}, {}, {}'.format(self.name, self.genre, self.instrument,
                                        self.biography))
