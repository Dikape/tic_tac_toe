from app import api
from app.hot_seat import resources as hot_seat_resources
from .auth import resources as auth_resources

api.add_resource(auth_resources.UserRegistrationResource, '/registration')
api.add_resource(auth_resources.UserInfoResource, '/user')
api.add_resource(hot_seat_resources.GameListResource, '/hot_seat')
api.add_resource(hot_seat_resources.StepsListResource, '/hot_seat/steps/<int:game_id>')
