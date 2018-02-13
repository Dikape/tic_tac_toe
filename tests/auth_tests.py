import os, sys
import unittest

sys.path.append(os.getcwd())

from app import app, db

from app.models import User



class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://beph:bephpass@localhost/tic_tac_toe_test')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        pass

    def test_login(self):
        pass


if __name__ == '__main__':
    unittest.main()