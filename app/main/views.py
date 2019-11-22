from . import main
from flask import render_template,request,redirect,url_for,abort


@main.route('/')
def index():
    '''
    View root function for the index.html page
    '''
    title = "HomePage"
    return render_template('index.html',title = title)