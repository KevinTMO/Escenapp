from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, DateTimeField
from wtforms.validators import DataRequired


class EventsForm(FlaskForm):
    """
    a form to update create, delete or update events
    """
    title = StringField('Title', validators=[DataRequired()])
    eventType = StringField('Event', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    hour = StringField('Hour', validators=[DataRequired()])

    submit = SubmitField('Post')
