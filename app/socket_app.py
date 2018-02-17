from app import sio


@sio.on('connect', namespace='/hot_seat')
def connect(sid, environ):
    pass


@sio.on('step', namespace='/hot_seat')
def step(sid, data):
    sio.emit('reply', data, namespace='/hot_seat', room=sid)


@sio.on('disconnect', namespace='/hot_seat')
def disconnect(sid):
    pass