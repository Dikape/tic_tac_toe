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
    help='Size (x*x) of board, where 15<=x<=100',
)

game_fields = {
    'id': fields.Integer,
    'size': fields.Integer,
}