from flask_restful import fields, reqparse

game_parser = reqparse.RequestParser()
game_parser.add_argument(
    'game_type', dest='game_type',
    required=True, location='json',
    help='One of types: "online", "hot_seat"',
)

game_parser.add_argument(
    'board_size', dest='board_size',
    required=True, location='json',
    help='Size (x*x) of board, where 15<=x<=30',
)

game_fields = {
    'id': fields.String,
    'uuid': fields.String,
    'size': fields.Integer,
    'author': fields.String,
    'game_type': fields.String,
    'finished_datetime': fields.String
}

step_fields = {
    'step_number': fields.Integer,
    'x_coordinate': fields.Integer,
    'y_coordinate': fields.Integer,
    'value': fields.String,
    'user': fields.String
}

history_fields = game_fields.copy()
history_fields['winner'] = fields.String

history_fields_with_steps = history_fields.copy()
history_fields_with_steps['steps'] = fields.Nested(step_fields)