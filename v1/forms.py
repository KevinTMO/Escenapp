from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from v1.models import User

class RegistrationForm(FlaskForm):
    """
    Creating the attrs to accept the information from the usr/artist
    """
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_email(self, email):
        """
        Validate if theres no duplicate email
        """
        userEmail = User.query.filter_by(email=email.data).first()

        if userEmail:
            raise ValidationError('An account using this email address already exists. Please choose another one')

class LoginForm(FlaskForm):
    """
    Creating the login attrs from the usr/artist
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')
