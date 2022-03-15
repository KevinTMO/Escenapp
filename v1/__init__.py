import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


# Configuration of flask plus secret key for our webapp security purpose

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = '73be4410e3006053dfe913a29efe79be'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_BINDS'] = {
    'dropquery': 'sqlite:///dropquery.db'
}

# Configuration for the database SQLAlchemy from flask plus Hashed pass

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Configuration for the login validation process

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Configuration for the sent email process

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from v1.users.routes import users
from v1.main.routes import main
from v1.posts.routes import posts
from v1.errors.handlers import errors

# Blueprints register

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(errors)
