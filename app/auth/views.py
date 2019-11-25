#pylint: skip-file
from flask import render_template,redirect,url_for,flash,request
from . import auth
from .forms import RegistrationForm
from .. import db
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm,RegistrationForm
from app.model import Users


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(email = form.email.data,username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)


@auth.route('/login',methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return render_template('index.html',login_form = form)


        flash ('Invalid username or password')

    title = "Pitch Perfect login"
    return render_template('auth/login.html',login_form= form,title = title)