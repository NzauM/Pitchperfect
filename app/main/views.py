#pylint: skip-file
from . import main
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .forms import PitchForm
from ..model import Users,Pitches


@main.route('/')
def index():
    '''
    View root function for the index.html page
    '''
    pitches = Pitches.query.all()
    business = Pitches.query.filter_by(category = 'business').all()
    technology = Pitches.query.filter_by(category = 'technology').all()
    education = Pitches.query.filter_by(category = 'education').all()
    return render_template("index.html", pitches = pitches, business = business, technology = technology, education = education)

@main.route('/pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        author = form.author.data

        new_pitch = Pitches(category = category,pitch= pitch,author = author)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    
    return render_template('new_pitches.html',PitchForm = form)
    
    

