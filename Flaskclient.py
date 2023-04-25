import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    print('1.Login')
    print('2.Send message')
    choice = input('')
    while choice != '1' and choice != '2':
        print('Please enter either 1 or 2')
    if choice == '1':
        print("Enter username")
        username = input('')
        print('User registered')
        sio.emit('register', username)
    else:
        print("What would you like to send")
        message = input('')
        sio.emit('message_r', message)


@sio.event
def disconnect():
    print('disconnected from server')
@sio.event
def messanger(sid, username):
    print(f"Welcome {sid} : {username}")

sio.connect('http://localhost:5001')
sio.wait()