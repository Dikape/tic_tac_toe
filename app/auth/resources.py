from flask_restful import fields, marshal_with, reqparse, Resource

from flask_jwt import jwt_required
from app.models import User

class UserRegistration(Resource):
    def post(self):
        return {'message': 'User registration'}