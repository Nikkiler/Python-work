import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

users = {'Bob': 'is cool'}
@sio.event
def join_room(sid):
    sio.enter_room(sid, 'chat_users')
@sio.event
def password_check(sid, username, password):
    if username in users:
        if users[username] == password:
            return username
        else:
            return 'Password or user are incorrect'
    else:
        return 'Password or user are incorrect'



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
def register(sid, username, password):
    users[username] = password
    print(f'{sid} {username}')


@sio.event
def message_r(sid, message, username):
    print(f'Message received {message} from {username}')
    sio.emit('my_reply',message ,room='chat_users')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)
