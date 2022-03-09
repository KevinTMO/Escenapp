from v1 import app, mail
from flask import url_for
from flask_mail import Message
from PIL import Image
import secrets
import os


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

def send_reset_email(user):
    """
    method to send a message when sending email for reset pass
    """
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@debugapocalypse.tech',
                  recipients=[user.email])

    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
