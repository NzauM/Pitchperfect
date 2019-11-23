#pylint: skip-file
from . import main
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required


@main.route('/')
def index():
    '''
    View root function for the index.html page
    '''
    title = "HomePage"
    return render_template('index.html',title = title)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    
    

