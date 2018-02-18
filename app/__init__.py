import socketio
from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
CORS(app)


from app.auth import security

api = Api(app, prefix="/api/v0")
jwt = JWT(app, security.authenticate, security.identity)
sio = socketio.Server()
migrate = Migrate(app, db)

from app import models, routes
from app.game import socket_app

