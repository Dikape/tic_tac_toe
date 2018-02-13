import os
from datetime import timedelta


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://beph:bephpass@localhost/tic_tac_toe'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'too_secret'
    JWT_AUTH_URL_RULE = '/api/v0/login'
    JWT_EXPIRATION_DELTA = timedelta(days=1)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://beph:bephpass@localhost/tic_tac_toe'


class DevelopmentConfig(Config):
    DEBUG = True


# class TestingConfig(Config):
