from datetime import datetime
from flask_restful import marshal_with, Resource, abort
from flask_jwt import jwt_required, current_identity
from sqlalchemy import desc

from app import models
from .parameters import game_parser, game_fields, step_fields


class OnlineGameListResource(Resource):
    @jwt_required()
    @marshal_with(game_fields)
    def get(self):
        """Get started games with single gamer"""
        games = []
        game_type = models.GameType.query.filter_by(title='online').first()
        games_qs = models.Game.query.filter_by(game_type_id=game_type.id,
                                               finished_datetime=None).all()
        for game in games_qs:
            if game.members.count() == 1:
                games.append(game)
        return games, 200

    def close_started_games(self):
        # TODO change it
        game_type_id = models.GameType.query.filter_by(title='online').first().id
        members = current_identity.members
        for member in members:
            current_game = member.game
            author_condition = current_identity.username == current_game.author
            not_finished_condition = current_game.finished_datetime is None
            type_condition = current_game.game_type_id == game_type_id
            if author_condition and not_finished_condition and type_condition:
                current_game.finished_datetime = datetime.now()
                current_game.save()

    @jwt_required()
    @marshal_with(game_fields)
    def post(self):
        args = game_parser.parse_args()
        self.close_started_games()
        game_type = models.GameType.query.filter_by(title=args.game_type).first()
        game = models.Game(size=args.board_size, game_type_id=game_type.id)
        game.save()
        member = models.Member(game_id=game.id, user_id=current_identity.id)
        member.save()

        return game, 201


class OnlineStepsListResource(Resource):
    @jwt_required()
    @marshal_with(step_fields)
    def get(self, game_id):
        members = models.Member.query.filter_by(game_id=game_id).all()
        members_id = [obj.id for obj in members]
        steps = models.Step.query. \
            filter(models.Step.member_id.in_(members_id)). \
            order_by(models.Step.step_number).all()
        return steps, 200
