def main():
    username = {}
    user_pass = {}
    while True:
        print("If you are an existing User Login if not please Register")
        print("1.Login")
        print("2.Register")
        choice = input()
        if choice == '1':
            break
        elif choice == '2':
            option1(username, user_pass)
            break
    menu()
    selection = (input(""))
    options = {'1' , '2' , '3', '4', '5', '6'}
    while selection not in options:
        menu()
        selection = (input(""))
    while selection != '6':
        if selection == '1':
            option1(username, user_pass)
            menu()
        elif selection == '5':
            option5(username)
            menu()
        elif selection == '4':
            option4(username)
            menu()
        selection = input("")

    print("Thank you for using our secret chat!")
def option1(username, passwords):
    userinput = input("Please, enter the username ")
    while len(userinput) == 0:
        userinput = input("Username is null please enter another name, please enter another name ")
    while userinput in username:
        userinput = input("Username already registered, please enter another name ")
        while len(userinput) == 0:
            userinput = input("Username is null please enter another name, please enter another name ")
    username[userinput] = "User"
    print("Please enter a password for this user:")
    password = input()
    passwords[userinput] = password
    print("User " + userinput + " registered")

def option4(username):
    print("Please enter username")
    changed_user = input()
    if changed_user in username:
        if username[changed_user] == "Admin":
                print("Error cannot downgrade Admin user")
        elif username[changed_user] != 'Admin':
            printpermissions()
            new_roll = input('')
            new_roll = conversion(new_roll)
            if new_roll != 'Admin' and new_roll != 'Moderator' and new_roll != 'User':
                new_roll = usertype(new_roll)
                new_roll = conversion(new_roll)
            username[changed_user] = new_roll
    else:
        print("This action will create a new user with chosen role")
        printpermissions()
        new_roll = input('')
        new_roll = conversion(new_roll)
        if new_roll != 'Admin' and new_roll != 'Moderator' and new_roll != 'User':
            new_roll = usertype(new_roll)
            new_roll = conversion(new_roll)
        username[changed_user] = new_roll
    print("User has either been created with permissions chosen or User permissions have been updated or u have left this option")


def option5(username):
    for user, permisions in username.items():
        print(user + " is a " + permisions)
def menu():
    print("please choose one of the following menu items")
    print("by choosing the corosponding menu item and hitting enter")
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. Assign role to existing user")
    print("5. List all registered users")
    print("6. Exit.")
def printpermissions():
    print("User types to change to or create are below")
    print("1. Admin")
    print("2. Moderator")
    print("3. User")
def usertype(new_role):
    while new_role != '1' and '2' and '3':
        printpermissions()
        new_role = input()
        if new_role == '1' or new_role == '2' or new_role == "3":
            break
    return new_role
def conversion(new_role):
    if new_role == '1':
        return 'Admin'
    elif new_role == '2':
        return 'Moderator'
    elif new_role == '3':
        return 'User'

if __name__ == '__main__':
    main()