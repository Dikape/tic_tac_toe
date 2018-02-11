from flask_restful import marshal_with, Resource, abort

from sqlalchemy.exc import IntegrityError

from app.models import User
from .parameters import user_fields, auth_parser


class UserRegistration(Resource):
    @marshal_with(user_fields)
    def post(self):
        args = auth_parser.parse_args()
        try:
            user = User(username=args.username, password=args.password).create()
            return user, 201
        except IntegrityError as e:
            abort(409, message='User with this name is exists!')

