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
def connect(sid, environ):
    print('connect', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event()
def write_to_file(users):
    with open('users.csv', 'w') as wf:
        fieldnames = ['Username', 'Password', 'Usertype']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for key, value in users.items():
            writer.writerow(value)
sio.emit('main', users)
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5001)), app)