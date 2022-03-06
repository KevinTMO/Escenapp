from v1 import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """
    this function should work the process of login/logout of the user
    by id
    """
    return Artist.query.get(int(user_id))

""" Below is the classes/attrs for the db  """

class Artist(db.Model, UserMixin):
    """
    sqltedb to store artist info
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # Adding below attrs to change in profile
    genre = db.Column(db.String(50))
    instrument = db.Column(db.String(50))
    biography = db.Column(db.String(150))

    def __repr__(self):
        """
        return repr string of Artist obj
        """
        return ('{}, {}, {}'.format(self.id, self.name, self.genre,
                                    self.instrument, self.biography))

class Gen(db.Model):
    """
    sql table just for genre column select field testing
    """
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(50))

    def __repr__(self):
        """
        return a repr of string objects
        """
        return "{}".format(self.genre)


class Inst(db.Model):
    """
    sql table just for instrument column select field testing
    """
    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String(50))

    def __repr__(self):
        """
        return a repr of string objects
        """
        return "{}".format(self.instrument)
