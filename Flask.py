
import socketio
import eventlet
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

users = {}

@sio.event
def connect(sid, environ, data):
    print('connect', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def login(sid, data):
    print(f"Login event {sid} {data}")
# @sio.event
# def message(message):
#     print(f"Message event {message}")
@sio.event
def register(sid, username):
    users[sid] = username
    sio.emit('messanger', sid, username)
@sio.event
def message_r(sid, message):
    print(f'Message recieved {message}')
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)