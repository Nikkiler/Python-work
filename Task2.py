def main():
    username = {"Bob": "Admin"}
    user_pass = {"Bob": "All_that_is_gold_does_not_glitter"}
    current_user = None
    while True:
        print("If you are an existing User Login if not please Register")
        print("1.Login")
        print("2.Register")
        choice = input()
        if choice == '1':
            register = login(username, user_pass)
            if register == False:
                current_user = option1(username, user_pass)
            else:
                current_user = register
            break

        elif choice == '2':
            current_user = option1(username, user_pass)
            break

    if username[current_user] != 'Admin':
        menu()
        selection = (input(""))
        options = {'1' , '2' , '3', '4'}
        while selection not in options:
            menu()
            selection = (input(""))
        while selection != '4':
            if selection == '1':
                current_user = option1(username, user_pass)
                menu()
                selection = input()
                if username[current_user] == 'Admin':
                    admin_account(username, user_pass, current_user)
                    break
            elif selection == '3':
                option5(username)
                menu()
                selection = input()
    if username[current_user] == "Admin":
        admin_account(username, user_pass, current_user)
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
    return userinput

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
    print("2. Connect to the chat")
    print("3. List all registered users")
    print("4. Exit.")
def admin_menu():
    print("please choose one of the following menu items")
    print("by choosing the corosponding menu item and hitting enter")
    print("1. Create a user")
    print("2. Connect to the chat")
    print("3. Change user role")
    print("4. List all registered users")
    print("5. Exit.")
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
def login(username, user_pass):
    print("please enter username")
    usercheck = input()
    while usercheck not in username:
        print("please enter a created user")
        print("if you would like to go back and register a user please press enter")
        usercheck = input()
        if len(usercheck) == 0:
            return False
            break
        elif usercheck in username:
            print("Welcome " + usercheck + " Please enter you password")
            passcheck = input()
            while user_pass[usercheck] != passcheck:
                print("Password is incorrect")
                print("Please enter correct password")
                passcheck = input()
            print("Welcome back " + usercheck)
            return usercheck
    if usercheck in username:
        print("Welcome " + usercheck + " Please enter you password")
        passcheck = input()
        while user_pass[usercheck] != passcheck:
            print("Password is incorrect")
            print("Please enter correct password")
            passcheck = input()
        print("Welcome back " + usercheck)
        return usercheck

def admin_account(username, user_pass, current_user):
    if username[current_user] == 'Admin':
        admin_menu()
        selection = (input(""))
        options = {'1' , '2' , '3', '4', '5'}
        while selection not in options:
            menu()
            selection = (input(""))
        while selection != '5':
            if selection == '1':
                current_user = option1(username, user_pass)
                menu()
                selection = input()
                if username[current_user] == 'Admin':
                    admin_account(username, user_pass, current_user)
                    break
            elif selection == '4':
                option5(username)
                menu()
                selection = input()
            elif selection == '3':
                option4(username)
                menu()
                selection = input("")


if __name__ == '__main__':
    main()