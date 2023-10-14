import socketio
import eventlet
import csv
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

users = {}
with open("users.csv", "r") as handler:
    reader = csv.DictReader(handler, delimiter=',')
    for row in reader:
        cr = row['Username']
        users[cr] = row
@sio.event
def join_room(sid):
    sio.enter_room(sid, 'chat_users')
@sio.event
def password_check(sid, username, password):
    if username in users:
        userd = users[username]
        passwords = userd['Password']
        if passwords == password:
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

@sio.event
def register(sid, username, password):
    users[username] = {'Username': username, 'Password': password, 'Usertype': 'User'}
    print(f'{sid} {username}')
    with open('users.csv', 'w') as wf:
        fieldnames = ['Username', 'Password', 'Usertype']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in users.items():
            writer.writerow(value)

@sio.event
def message_r(sid, message, username):
    print(f'Message received {message} from {username}')
    sio.emit('my_reply',message ,room='chat_users')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)
