import socketio

sio = socketio.Client()
username = None


@sio.event
def connect():
    print('connection established')
    sio.emit('join_room')
    main_menu()
@sio.event
def my_reply(data):
    print(f'message from server {data}')


@sio.event
def disconnect():
    print('disconnected from server')
def main_menu():
    print('1.Register')
    print('2.Login')
    print('3.Chat')
    choice = input('')
    while choice != '1' and choice != '2' and choice != '3':
        print('Please enter either 1 or 2 or 3')
        choice = input('')
    username = None
    if choice == '1':
        username = option1()
    elif choice == '2':
        username = option2()
    elif choice == '3':
        username = chat(username)

def login():
    print("Login to server, send data to server")

def register():
    print("Register")

def send_message():
    print("")

def option1():
    print("Enter username")
    username = input('')
    print('Please enter a password')
    password = input('')
    print('User registered')
    sio.emit('register',(username, password))
    chat(username)


def chat(username):
    print(f'Welcome {username}')
    print("What would you like to send")
    message = input('')
    sio.emit('message_r', (message, username))
    print('would you like to exit? y/n')
    answer = input('')
    answer = answer.lower()
    while answer != 'y':
        print("What would you like to send")
        message = input('')
        sio.emit('message_r', (message, username))
        print('would you like to exit? y/n')
        answer = input('')
        answer = answer.lower()


def check(data):
    if data == 'Password or user are incorrect':
        print('Password or user are incorrect')
        current_user = option2()
    else:
        chat(data)

def option2():
    while True:
        print('Enter Username')
        current_user = input('')
        print("Enter password")
        print('Press enter if you would like to go back to main menu')
        password = input('')
        if len(password) == 0:
            main_menu()
            break
        sio.emit('password_check', (current_user, password), callback=check)
        return current_user
sio.connect('http://localhost:5001')
sio.wait()
