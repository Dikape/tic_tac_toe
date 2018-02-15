import eventlet
import socketio
from app import app, sio

if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    # app.run(host='0.0.0.0')
    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
