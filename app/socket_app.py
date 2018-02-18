from app import sio

from app import models
from .calculations import check_winner


@sio.on('connect', namespace='/hot_seat')
def connect(sid, environ):
    pass


@sio.on('step', namespace='/hot_seat')
def step(sid, data):
    current_symbol = data['currentSymbol']
    member = models.Member.query.filter_by(game_id=data['gameId'], user_id=data['userId']).first()
    step = models.Step(step_number=data['stepNumber'],
                       x_coordinate=data['x'],
                       y_coordinate=data['y'],
                       value=current_symbol,
                       member_id=member.id)
    step.save()
    step_coordinate = (step.x_coordinate, step.y_coordinate)
    all_steps = member.steps.filter_by(value=current_symbol).\
        order_by(models.Step.step_number).\
        with_entities(models.Step.x_coordinate, models.Step.y_coordinate).all()

    is_winner = check_winner(all_steps, step_coordinate)
    response = {'message': 'saved'}
    if is_winner:
        response['message'] = '{0} winner!'.format(current_symbol)
    sio.emit('step_result', response, namespace='/hot_seat', room=sid)


@sio.on('disconnect', namespace='/hot_seat')
def disconnect(sid):
    pass