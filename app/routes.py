from app import api
from app.game import resources as resources

from .auth import resources as auth_resources

api.add_resource(auth_resources.UserRegistrationResource, '/registration')
api.add_resource(auth_resources.UserInfoResource, '/user')
api.add_resource(resources.HotSeatGameListResource, '/hot_seat')
api.add_resource(resources.HotSeatStepsListResource, '/hot_seat/steps/<int:game_id>')
api.add_resource(resources.OnlineGameListResource, '/online')
api.add_resource(resources.HistoryListResource, '/finished_games')
