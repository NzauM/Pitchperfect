#pylint: skip-file
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..model import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Enter email adress',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Create a password',validators=[Required(),EqualTo('password_confirm',message= 'The passwords must be the same')])
    password_confirm = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("An account with that email already exists")

    def validate_username(self,dara_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is taken")

class Login_form(FlaskForm):
    email = StringField('Enter Email adress',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')
