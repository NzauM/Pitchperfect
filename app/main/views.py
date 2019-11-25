#pylint: skip-file
from . import main
from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm,UpdateProfile
from ..model import Users,Pitches,Comments
from app import db,photos


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


@main.route('/user/<usernam>/update',methods = ['GET','POST'])
@login_required
def update_profile(usernam):
    user = Users.query.filter_by(username = usernam).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',usernam = user.username))

    return render_template('profile/update.html',form = form)

@main.route('/user/<usernam>/update/pic',methods=['POST'])
@login_required
def update_pic(usernam):
    user = Users.query.filter_by(username = usernam).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',usernam = usernam))

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



    
    

