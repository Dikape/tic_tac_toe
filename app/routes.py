from app import api

from .auth import resources as auth_resources
from .hot_seat import resources as hot_seat_resources

api.add_resource(auth_resources.UserRegistrationResource, '/registration')
api.add_resource(auth_resources.UserInfoResource, '/user')
api.add_resource(hot_seat_resources.Game, '/hot_seat')
