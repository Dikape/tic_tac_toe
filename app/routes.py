from app import api
from app.hot_seat import resources as hot_seat_resources
from app.online import resources as online_resources
from .auth import resources as auth_resources

api.add_resource(auth_resources.UserRegistrationResource, '/registration')
api.add_resource(auth_resources.UserInfoResource, '/user')
api.add_resource(hot_seat_resources.HotSeatGameListResource, '/hot_seat')
api.add_resource(hot_seat_resources.HotSeatStepsListResource, '/hot_seat/steps/<int:game_id>')
api.add_resource(online_resources.OnlineGameListResource, '/online')
