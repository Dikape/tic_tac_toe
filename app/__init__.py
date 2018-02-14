from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt import JWT
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
CORS(app)

from app.auth import security

api = Api(app, prefix="/api/v0")
jwt = JWT(app, security.authenticate, security.identity)
migrate = Migrate(app, db)

from app import models, routes


