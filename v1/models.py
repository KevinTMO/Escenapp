from v1 import db, login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


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
    posts = db.relationship('PostEvent', backref='event', lazy=True)


    def get_reset_token(self, expires_sec=1800):
        """
        Generating a token that expires every 3 mins by def
        Can pass a value to overwrite that value for another
        """
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """
        Method to verify the token or if its expired
        """
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Artist.query.get(user_id)

    def __repr__(self):
        """
        return repr string of Artist obj
        """
        return ('{}, {}, {}'.format(self.id, self.name, self.genre,
                                    self.instrument, self.biography))

class PostEvent(db.Model):
    """
    table to stored artist events information
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    eventType = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    hour = db.Column(db.String(25), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)


    def __repr__(self):
        """
        return a repr str of data in table
        """
        return ('{}, {}, {}'.format(self.title, self.date, self.artist_id))


class Gen(db.Model):
    """
    sql table just for genre column select field testing
    """
    __bind_key__ = 'dropquery'
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
    __bind_key__ = 'dropquery'
    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String(50))

    def __repr__(self):
        """
        return a repr of string objects
        """
        return "{}".format(self.instrument)
