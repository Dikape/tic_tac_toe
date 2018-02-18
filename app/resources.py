from flask_restful import marshal_with, Resource, abort
from flask_jwt import jwt_required, current_identity
from sqlalchemy import desc

from app import models
from .parameters import game_parser, game_fields, step_fields


class GameListResource(Resource):
    @jwt_required()
    @marshal_with(game_fields)
    def get(self):
        """Get last game for current user"""
        member = current_identity.members.order_by(desc(models.Member.id)).first()
        game = models.Game.query.filter_by(id=member.game_id).first()
        return game, 200

    @jwt_required()
    @marshal_with(game_fields)
    def post(self):
        args = game_parser.parse_args()
        game_type = models.GameType.query.filter_by(title=args.game_type).first()
        game = models.Game(size=args.board_size, game_type_id=game_type.id)
        game.save()
        member = models.Member(game_id=game.id, user_id=current_identity.id)
        member.save()
        return game, 201


class StepsListResource(Resource):
    @jwt_required()
    @marshal_with(step_fields)
    def get(self, game_id):
        members = models.Member.query.filter_by(game_id=game_id).all()
        members_id = [obj.id for obj in members]
        steps = models.Step.query.\
            filter(models.Step.member_id.in_(members_id)).\
            order_by(models.Step.step_number).all()
        return steps, 200
