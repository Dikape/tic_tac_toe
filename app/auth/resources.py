from flask_restful import marshal_with, Resource, abort
from flask_jwt import jwt_required, current_identity

from app import jwt
from app.models import User
from .parameters import (user_fields,
                         auth_user_fields,
                         auth_parser)


class UserRegistrationResource(Resource):
    @marshal_with(auth_user_fields)
    def post(self):
        args = auth_parser.parse_args()
        user_with_username = User.query.filter_by(username=args.username).all()
        if user_with_username:
            abort(409, message='User with this name is exists!')

        user = User(username=args.username, password=args.password).create()
        access_token = jwt.jwt_encode_callback(user).decode('utf8')
        response = {
                'id': user.id,
                'username': user.username,
                'access_token': access_token,
        }
        return response, 201


class UserInfoResource(Resource):
    @jwt_required()
    @marshal_with(user_fields)
    def get(self):
        return current_identity, 200
