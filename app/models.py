from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    members = db.relationship('Member', backref='user', lazy=True)

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


class GameType(db.Model):
    __tablename__ = 'game_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(10))
    games = db.relationship('Game', backref='game_type', lazy=True)


class Game(db.Model):
    __tablename__ = 'game'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Integer)
    game_type_id = db.Column(db.Integer, db.ForeignKey('game_type.id'), nullable=False)
    members = db.relationship('Member', backref='game', lazy=True)


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(20))


class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=True)
    steps = db.relationship('Step', backref='member', lazy=True)


class Step(db.Model):
    __tablename__ = 'step'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    step_number = db.Column(db.Integer)
    x_coordinate = db.Column(db.Integer)
    y_coordinate = db.Column(db.Integer)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)


