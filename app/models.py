from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    games = db.relationship('Game', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def create(self):
        self.set_password(self.password)
        db.session.add(self)
        db.session.commit()
        return self


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Integer)
    members = db.relationship('Member', backref='game', lazy=True)


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(20))


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=True)
    steps = db.relationship('Step', backref='member', lazy=True)


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    step_number = db.Column(db.Integer)
    x_coordinate = db.Column(db.Integer)
    y_coordinate = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)


