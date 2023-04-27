import socketio
sio = socketio.Client()
users = {}
@sio.event
def connect():
    print('connection established')
    print('1.Register')
    print('2.Login')
    choice = input('')
    while choice != '1' and choice != '2':
        print('Please enter either 1 or 2')
    if choice == '1':
        option1()
    elif choice == '2':
        option3()


@sio.event
def disconnect():
    print('disconnected from server')
def option1():
    print("Enter username")
    username = input('')
    print('Please enter a password')
    password = input('')
    print('User registered')
    sio.emit('register', [username, password])
    print(f'Welcome {username}')
    print("What would you like to send")
    message = input('')
    sio.emit('message_r', [message, username])
    print('would you like to exit? y/n')
    answer = input('')
    answer = answer.lower()
    while answer != 'y':
        print("What would you like to send")
        message = input('')
        sio.emit('message_r', [message, username])
        print('would you like to exit? y/n')
        answer = input('')
        answer = answer.lower()
    users[username] = password
def option2(username):
    print("What would you like to send")
    message = input('')
    sio.emit('message_r', message, username)
    print('would you like to exit? y/n')
    answer = input('')
    answer = answer.lower()
    while answer != 'y':
        print("What would you like to send")
        message = input('')
        sio.emit('message_r', message, username)
        print('would you like to exit? y/n')
        answer = input('')
        answer = answer.lower()
def option3():
    print('Enter Username')
    current_user = input('')
    if current_user in users:
        print('Enter password')
        password = input('')
        while users[current_user] != password:
            print('Please enter correct password')
            password = input('')
        print(f"Welcome {current_user}")
        option2(current_user)
sio.connect('http://localhost:5001')
sio.wait()