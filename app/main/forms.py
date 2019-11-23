#pylint: skip-file
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = StringField('Category of your review',validators=[Required()])
    pitch = TextAreaField('Your Pitch' validators=[Required()])
    Author = StringField('Your name' validators=[Required()])
    submit = SubmitField('Submit')