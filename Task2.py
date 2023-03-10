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
                    print("Change to")
                    print("1. Admin")
                    print("2. Moderator")
                    print("3. User")
                    new_roll = input()
                    username[changed_user2] = new_roll
                    break
                elif changed_user2 not in username:
                    print("This action will create a new user with chosen role")
                    print("1. Admin")
                    print("2. Moderator")
                    print("3. User")
                    new_roll = input()
                    username[changed_user] = new_roll
                    break
        elif username[changed_user] != 'Admin':
            print("Change to")
            print("1. Admin")
            print("2. Moderator")
            print("3. User")
            new_roll = input()
            username[changed_user] = new_roll


    else:
        print("This action will create a new user with chosen role")
        print("1. Admin")
        print("2. Moderator")
        print("3. User")
        new_roll = input()
        username[changed_user] = new_roll


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
class Admin:
    def __init__(self, name, ):
        self.name = name
class Moderator:
    def __init__(self, name, ):
        self.name = name
class User:
    def __init__(self, name, ):
        self.name = name
if __name__ == '__main__':
    main()