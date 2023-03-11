def main():
    username = {}
    menu()
    selection = (input(""))
    options = {'1' , '2' , '3', '4', '5', '6'}
    while selection not in options:
        menu()
        selection = (input(""))
    while selection != '6':
        if selection == '1':
            option1(username)
            menu()
        elif selection == '5':
            option5(username)
            menu()
        elif selection == '4':
            option4(username)
            menu()
        selection = input("")

    print("Thank you for using our secret chat!")
def option1(username):
    userinput = input("Please, enter the username ")
    while len(userinput) == 0:
        userinput = input("Username is null please enter another name, please enter another name ")
    while userinput in username:
        userinput = input("Username already registered, please enter another name ")
        while len(userinput) == 0:
            userinput = input("Username is null please enter another name, please enter another name ")
    username[userinput] = "User"
    print("User " + userinput + " registered")

def option4(username):
    print("Please enter username")
    changed_user = input()
    if changed_user in username:
        if username[changed_user] == "Admin":
            while True:
                print("Error cannot downgrade Admin user")
                print("Please choose new user")
                changed_user2 = input()
                if changed_user != changed_user2 and changed_user2 in username and username[changed_user2] != 'Admin':
                    changed_user = changed_user2
                    userpermissions()
                    new_roll = input('')
                    if new_roll != 'Admin' or new_roll != 'Moderator' or new_roll != 'User':
                        new_roll = usertype(new_roll)
                    username[changed_user] = new_roll
                    break
                elif changed_user2 not in username:
                    print("This action will create a new user with chosen role")
                    userpermissions()
                    new_roll = input('')
                    if new_roll != 'Admin' or new_roll != 'Moderator' or new_roll != 'User':
                        new_roll = usertype(new_roll)
                    username[changed_user2] = new_roll
                    break
        elif username[changed_user] != 'Admin':
            userpermissions()
            new_roll = input('')
            if new_roll != 'Admin' or new_roll != 'Moderator' or new_roll != 'User':
                new_roll = usertype(new_roll)
            username[changed_user] = new_roll
    else:
        print("This action will create a new user with chosen role")
        userpermissions()
        new_roll = input('')
        if new_roll != 'Admin' or new_roll != 'Moderator' or new_roll != 'User':
            new_roll = usertype(new_roll)
        username[changed_user] = new_roll
    print("User has either been created with permissions chosen or User permissions have been updated")


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
def userpermissions():
    print("User types to change to or create are below")
    print("Also please keep in mind to enter the name rather than the number of the user type")
    print("1. Admin")
    print("2. Moderator")
    print("3. User")
def usertype(new_role):
    while new_role != 'Admin' or 'Moderator' or 'User':
        userpermissions()
        new_role = input()
        if new_role == 'Admin' or new_role == 'Moderator' or new_role == "User":
            break
    return new_role
if __name__ == '__main__':
    main()