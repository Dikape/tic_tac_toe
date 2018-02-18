from app import sio

from app import models
from .calculations import check_winner


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
    return response

@sio.on('connect', namespace='/hot_seat')
def connect(sid, environ):
    pass


@sio.on('step', namespace='/hot_seat')
def step(sid, data):
    member = models.Member.query.filter_by(game_id=data['gameId'], user_id=data['userId']).first()
    step = models.Step(step_number=data['stepNumber'],
                       x_coordinate=data['x'],
                       y_coordinate=data['y'],
                       value=data['currentSymbol'],
                       member_id=member.id)
    step.save()
    response = get_game_result(step, member)
    sio.emit('step_result', response, namespace='/hot_seat', room=sid)


@sio.on('disconnect', namespace='/hot_seat')
def disconnect(sid):
    pass