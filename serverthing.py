import socketio
sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
@sio.event
def connect(sid, environ, data):
    print('connect', sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

@sio.event
def login(sid, data):
    print(f"Login event {sid} {data}")