import csv
def main():
    current_user = None
    cr = None
    users = {}
    with open("users.csv", "r") as handler:
        reader = csv.DictReader(handler, delimiter=',')
        for row in reader:
            print(row)
            cr = row['Username']
            users[cr] = row
    while True:
        print("If you are an existing User Login if not please Register")
        print("1.Login")
        print("2.Register")
        choice = input()
        if choice == '1':
            register = login(users)
            if register == False:
                current_user = option1(users)
            else:
                current_user = register
            break

        elif choice == '2':
            current_user = option1(users)
            break

    if users[current_user["Usertype"]] != 'Admin':
        non_admin_account(users, current_user)
    elif users[current_user["Usertype"]] == "Admin":
        admin_account(users, current_user)
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
    with open('users.csv', 'r+') as rwf:
        rwf.write("\n" + userinput + ",")
        rwf.write(password + ",")
        rwf.write(username[userinput])
    print("Would you like to switch to this user? Y/N")
    yes_r_no = input("")
    yes_r_no = yes_r_no.lower()
    while yes_r_no != 'y' and yes_r_no != 'n':
        print("please enter either Y or N")
        yes_r_no = input("")
        yes_r_no = yes_r_no.lower()
    if yes_r_no == "y":
        return userinput
    else:
        return False


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
        print("Please enter a password for this user:")
        password = input()
        with open('users.txt', 'r+') as rwf:
            rwf.write(changed_user + "\n")
            rwf.write(password + "\n")
            rwf.write(username[changed_user] + "\n")
    print("User has either been created with permissions chosen or User permissions have been updated or u have left this option")


def option5(users):
    for user, permisions in users.items():
        print(users + " is a " + permisions[user["Usertype"]])
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
def login(users):
    print("please enter username")
    usercheck = input()
    while usercheck not in users:
        print("please enter a created user")
        print("if you would like to go back and register a user please press enter")
        usercheck = input()
        if len(usercheck) == 0:
            return False
            break
        elif usercheck in users:
            print("Welcome " + usercheck + " Please enter you password")
            passcheck = input()
            while users[usercheck["Password"]] != passcheck:
                print("Password is incorrect")
                print("Please enter correct password")
                passcheck = input()
            print("Welcome back " + usercheck)
            return usercheck
    if usercheck in users:
        print("Welcome " + usercheck + " Please enter you password")
        passcheck = input()
        while users[usercheck["Password"]] != passcheck:
            print("Password is incorrect")
            print("Please enter correct password")
            passcheck = input()
        print("Welcome back " + usercheck)
        return usercheck

def admin_account(users, current_user):
    if users[current_user["Usertype"]] == 'Admin':
        admin_menu()
        selection = (input(""))
        options = {'1' , '2' , '3', '4', '5'}
        while selection not in options:
            admin_menu()
            selection = (input(""))
        while selection != '5':
            if selection == '1':
                previouse_user = current_user
                current_user = option1(users)
                if current_user == False:
                    current_user = previouse_user
                    admin_account(users, current_user)
                    break
                elif users[current_user["Usertype"]] == 'Admin':
                    admin_account(users, current_user)
                    break
                else:
                    admin_account(users, current_user)

            elif selection == '4':
                option5(users)
                admin_account(users, current_user)
                break
            elif selection == '3':
                option4(users)
                admin_account(users, current_user)
                break
def non_admin_account(users, current_user):
    current_user = current_user
    menu()
    selection = (input(""))
    options = {'1', '2', '3', '4'}
    while selection not in options:
        menu()
        selection = (input(""))
    while selection != '4':
        if selection == '1':
            current_user = option1(users)
            menu()
            selection = input()
            if users[current_user["Usertype"]] == 'Admin':
                admin_account(users, current_user)
                break
        elif selection == '3':
            option5(users)
            menu()
            selection = input()
if __name__ == '__main__':
    main()