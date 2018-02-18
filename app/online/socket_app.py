import socketio
from datetime import datetime
from app import sio
from app import models
from app.calculations import check_winner


def get_steps(members) -> list:
    steps = list()
    members_id = [obj.id for obj in members]
    steps_qs = models.Step.query. \
        filter(models.Step.member_id.in_(members_id)).\
        order_by(models.Step.step_number).all()
    for step in steps_qs:
        steps.append({
            'step_number': step.step_number,
            'x_coordinate': step.x_coordinate,
            'y_coordinate': step.y_coordinate,
            'value': step.value,
        })
    return steps


def get_game_result(step, member):
    response = {'message': 'saved'}
    game = member.game
    all_steps = member.steps.order_by(models.Step.step_number)
    all_steps_current_symbol = all_steps.filter_by(value=step.value).\
        with_entities(models.Step.x_coordinate, models.Step.y_coordinate).all()

    step_coordinate = (step.x_coordinate, step.y_coordinate)
    is_winner = check_winner(all_steps_current_symbol, step_coordinate)

    if is_winner:
        response['message'] = '{0} winner!'.format(step.value)
    elif len(all_steps.all()) == game.size*game.size:
        response['message'] = 'Draw game!'
    if response['message'] != 'saved':
        game.finished_datetime = datetime.now()
        game.save()
    return response


class OnlineGameNamespace(socketio.Namespace):
    def on_connect(self, sid, environ):
        pass

    def on_connect_to_game(self, sid, data):
        game = models.Game.query.filter_by(uuid=data['gameUUID']).first()
        members_user_id = [member.user_id for member in game.members]
        current_user = models.User.query.filter_by(id=data['userId']).first()
        game_data = {
            'board_size': game.size,
            'game_id': game.id,
            'author': game.author,
            'steps': get_steps(game.members)
        }
        if current_user.id in members_user_id:
            self.enter_room(sid, room=data['gameUUID'])
            self.emit('game_info', game_data, room=sid)
        else:
            members_count_condition = game.members.count() == 1
            not_finished_condition = game.finished_datetime is None
            if members_count_condition and not_finished_condition:
                member = models.Member(game_id=game.id,user_id=current_user.id)
                member.save()
                sio.enter_room(sid, data['gameUUID'])
                self.emit('game_info', game_data, room=sid)
            else:
                self.emit('cant_connect', {'message': 'Create new game or choose other!'}, room=sid)

    def on_get_result(self, sid, data):
        member = models.Member.query.filter_by(game_id=data['gameId'], user_id=data['userId']).first()
        step = models.Step(step_number=data['stepNumber'],
                           x_coordinate=data['x'],
                           y_coordinate=data['y'],
                           value=data['currentSymbol'],
                           member_id=member.id)
        step.save()
        response = get_game_result(step, member)
        self.emit('game_result', response, room=data['gameUUID'])

    def on_step(self, sid, data):
        self.emit('step_result', data, room=data['gameUUID'])

    def on_disconnect(self, sid):
        pass

sio.register_namespace(OnlineGameNamespace('/online'))