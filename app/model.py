#pylint: skip-file
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_manager
from flask_login import UserMixin


# login_manager = LoginManager()



class Users(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    @property
    def password(self):
        raise AttributeError('Password cannot be read')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return Users.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'


class Pitches(db.Model):
    __tablename__ = "pitches"

    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.String)
    author = db.Column(db.String)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
