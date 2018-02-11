from app import api

from .auth import resources as auth_resources

api.add_resource(auth_resources.UserRegistration, '/registration')
