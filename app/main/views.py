#pylint: skip-file
from . import main
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm
from ..model import Users,Pitches,Comments


@main.route('/')
def index():
    '''
    View root function for the index.html page
    '''
    
    return render_template('index.html')

@main.route('/viewPitches/<category>')
def viewPitches(category):
    '''
    View root function for the viewPitches.html page
    '''
    pitches = Pitches.view_pitches(category)

       
    return render_template('viewPitches.html',category=category,pitches=pitches)

    
@main.route('/new_pitches', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        author = form.author.data

        new_pitch = Pitches(category = category,pitch= pitch,author = author,user = current_user.username)
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    
    return render_template('new_pitches.html',PitchForm = form)

@main.route('/user/<usernam>')
def profile(usernam):
    user = Users.query.filter_by(username = usernam).first()

    pitches=Pitches.get_user_pitches(user.username)
    # print("___________***********************************_________________")
    # print(pitches)
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user,pitches=pitches)


@main.route('/pitch,<id>')
@login_required
def pitch(id):
    pitch = Pitches.query.filter_by(id = id).first()

    comment = Comments.get_comments()
    return render_template('viewPitches.html',pitch = pitch,comment = comment)


@main.route('/comment/<int:id>', methods = ['GET', 'POST'])
def comment(id):

    form = CommentForm()
    
    if form.validate_on_submit():
        comment = form.comment.data
        
        new_comment = Comments(comment = comment,user = current_user.username,pitch_id=id)

        new_comment.save_comment()

        return redirect(url_for('main.index', id = id))

    return render_template('comment.html',commentForm= form)



    
    

