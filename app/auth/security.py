from werkzeug.security import safe_str_cmp
from app.models import User


def authenticate(username, password):
    user = User.query.filter(username=username).fir
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)