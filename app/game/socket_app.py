import socketio
from datetime import datetime
from app import sio
from app import models
from app.calculations import check_winner


def save_member_status(member, status_str):
    members = member.game.members
    if status_str == 'winner':
        status_winner = models.Status.query.filter_by(status=status_str).first()
        status_loser = models.Status.query.filter_by(status='loser').first()
        member.status_id = status_winner.id
        member.save()
        members.remove(member)
        loser_member = members[0]
        loser_member.status_id = status_loser.id
        loser_member.save()
    else:
        status_draw = models.Status.query.filter_by(status='draw').firsrt()
        for member_obj in members:
            member_obj.status_id = status_draw.id
            member_obj.save()


def get_game_result(step, member):
    response = {'message': 'saved'}
    game = member.game
    all_steps = member.steps.order_by(models.Step.step_number)
    all_steps_current_symbol = all_steps.filter_by(value=step.value).\
        with_entities(models.Step.x_coordinate, models.Step.y_coordinate).all()

    step_coordinate = (step.x_coordinate, step.y_coordinate)
    is_winner = check_winner(all_steps_current_symbol, step_coordinate)

    if is_winner:
        save_member_status(member, 'winner')
        response['message'] = '{0} winner!'.format(step.value)
    elif len(all_steps.all()) == game.size*game.size:
        save_member_status(member, 'draw')
        response['message'] = 'Draw game!'
    if response['message'] != 'saved':
        game.finished_datetime = datetime.now()
        game.save()
    return response


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


class HotSeatGameNamespace(socketio.Namespace):
    def on_connect(self, sid, environ):
        pass

    def on_step(self, sid, data):
        member = models.Member.query.filter_by(game_id=data['gameId'], user_id=data['userId']).first()
        step = models.Step(step_number=data['stepNumber'],
                           x_coordinate=data['x'],
                           y_coordinate=data['y'],
                           value=data['currentSymbol'],
                           member_id=member.id)
        step.save()
        response = get_game_result(step, member)
        sio.emit('step_result', response, namespace='/hot_seat', room=sid)

    def on_disconnect(self, sid):
        pass

sio.register_namespace(HotSeatGameNamespace('/hot_seat'))


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
        not_finished_condition = game.finished_datetime is None
        if not_finished_condition:
            if current_user.id in members_user_id:
                self.enter_room(sid, room=data['gameUUID'])
                self.emit('game_info', game_data, room=sid)
            elif game.members.count() == 1:
                member = models.Member(game_id=game.id,user_id=current_user.id)
                member.save()
                sio.enter_room(sid, data['gameUUID'])
                self.emit('game_info', game_data, room=sid)
            else:
                self.emit('cant_connect', {'message': 'Create new game or choose another!'}, room=sid)
        else:
            game_data['finished'] = 'Game finished'
            self.emit('game_info', game_data, room=sid)

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