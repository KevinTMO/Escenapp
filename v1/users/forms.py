from wtforms_sqlalchemy.fields import QuerySelectField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from v1.models import Artist, Gen, Inst


def genSl():
    """
    return query genre
    """
    return Gen.query

def insSl():
    """
    return query instrument
    """
    return Inst.query


class RegistrationForm(FlaskForm):
    """
    Creating the attrs to accept the information from the usr/artist
    """
    name = StringField('Artist Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # Below testing extra info attrs
    # genre = StringField('Genre', validators=[DataRequired(), Length(max=20)])
    instrument = QuerySelectField(query_factory=insSl, allow_blank=True, get_label='instrument')
    genre = QuerySelectField(query_factory=genSl, allow_blank=True, get_label='genre')
    # biography = StringField('Biography', validators=[DataRequired(), Length(max=150)])
    # attr for sign up button
    submit = SubmitField('Sign Up')


    # validate if email already exist
    def validate_email(self, email):
        """
        Validate if theres no duplicate email
        """
        artistEmail = Artist.query.filter_by(email=email.data).first()

        if artistEmail:
            raise ValidationError('An account using this email address already exists. Please choose another one')



class LoginForm(FlaskForm):
    """
    Creating the login attrs from the usr/artist
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class UpdateAccountForm(FlaskForm):
    """
    Creating the attrs to accept the information from the usr/artist
    """
    biography = StringField('Biography', validators=[Length(max=150)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

class UpdateEmailForm(FlaskForm):
    """
    Creating the attrs to accept the information from the usr/artist
    """
    email = StringField('Email', validators=[Email()])

    def validate_email(self, email):
        """
        Validate if theres no duplicate email
        """
        if email.data != current_user.email:
            artistEmail = Artist.query.filter_by(email=email.data).first()
            if artistEmail:
                raise ValidationError('An account using this email address already exists. Please choose another one')


class RequestResetForm(FlaskForm):
    """
    Creating a form for request reset password
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


    def validate_email(self, email):
        """
        Validate if the email exists in our database
        """
        artistEmail = Artist.query.filter_by(email=email.data).first()

        if artistEmail is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    """
    from to reset password after authorization
    """
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
