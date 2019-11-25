#pylint: skip-file
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    category = SelectField(u'Select Category',choices=[('Business','Business'),('Technology','Technology'),('Education','Education')])
    pitch = TextAreaField('Your Pitch' ,validators=[Required()])
    author = StringField('Your name' ,validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = StringField('Your Comment',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('A brief bio',validators = [Required()])
    submit = SubmitField('Submit')