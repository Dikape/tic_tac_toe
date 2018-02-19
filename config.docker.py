import os
from datetime import timedelta


class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://tic_tac_toe_user:tic_tac_toe_pass@postgres_db/tic_tac_toe_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'too_secret'
    JWT_AUTH_URL_RULE = '/api/v0/login'
    JWT_EXPIRATION_DELTA = timedelta(days=1)


class DevelopmentConfig(Config):
    DEBUG = True


# class TestingConfig(Config):
