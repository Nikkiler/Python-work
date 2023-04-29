import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

users = {'Bob': 'is cool'}

@sio.event
def user_check(sid, username):
    if username in users:
        return 'user in users'
@sio.event
def password_check(sid, tuple):
    username = tuple[0]
    password = tuple[1]
    if users[username] == 'password':
        return 'Password is correct'


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
def register(sid, user):
    username = user[0]
    password = user[1]
    users[username] = password
    print(f'{sid} {username}')


@sio.event
def message_r(sid, message):
    username = message[1]
    messages = message[0]
    print(f'Message received {messages} from {username}')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)
