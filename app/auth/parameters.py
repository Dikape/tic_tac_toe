from flask_restful import fields, reqparse

auth_parser = reqparse.RequestParser()
auth_parser.add_argument(
    'username', dest='username',
    required=True, location='json',
    help='The user\'s username',
)

auth_parser.add_argument(
    'password', dest='password',
    required=True, location='json',
    help='The user\'s password',
)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
}
