import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://beph:bephpass@localhost/tic_tac_toe'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'too_secret'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://beph:bephpass@localhost/tic_tac_toe'


class DevelopmentConfig(Config):
    DEBUG = True
