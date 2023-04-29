import socketio

sio = socketio.Client()
username = None


@sio.event
def connect():
    print('connection established')
    main_menu()



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
    sio.emit('user_register',)


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


def option2():
    print('Enter Username')
    current_user = input('')
    sio.emit('user_check', current_user, callback=password_check)
    return current_user
def password_check():
    while True:
        print("Enter password")
        print('Press enter if you would like to go back to main menu')
        password = input('')
        if len(password) == 0:
            main_menu()
        else:
            sio.emit('password_check', (username, password), callback=chat)
sio.connect('http://localhost:5001')
sio.wait()
