#pylint: skip-file
import unittest
from app.model import Users

class UserTest(unittest.TestCase):

    def setUp(self):
        self.new_user = Users(password = 'MERCY')


    def test_password(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_read_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_verify_password(self):
        self.assertTrue(self.new_user.verify_password('MERCY'))