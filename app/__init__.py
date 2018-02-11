from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt import JWT

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)


from app.auth import security

api = Api(app, prefix="/api/v0")
jwt = JWT(app, security.authenticate, security.identity)
migrate = Migrate(app, db)

from app import models


