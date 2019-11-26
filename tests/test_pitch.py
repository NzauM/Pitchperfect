#pylint: skip-file
import unittest
from app.models import Pitch, User
from flask_login import current_user
from app import db

class TestPitch(unittest.TestCase):

    def setUp(self):
        self.user_joe = User(username='mercy',password='password',email='abc@defg.com')
        self.new_pitch = Pitch(pitch_content = "This is my pitch", pitch_category='Business',user=self.user_mercy)
    
    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()
        # my_user = db.session.query(User).filter(self.user.id==1).first()
        # db.session.delete(my_user)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_content,"This is my pitch")
        self.assertEquals(self.new_pitch.pitch_category,'Business')
        self.assertEquals(self.new_pitch.user,self.user_mercy)


    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_all_pitches(self):
        self.new_pitch.save_pitch()
        get_pitches = Pitch.get_all_pitches()
        self.assertTrue(len(get_pitches)==1)