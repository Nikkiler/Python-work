def main():
    username = set()
    selection = (input("Welcome to the secret chat please choose one of the following menu items by choosing the corosponding menu item and hitting enter 1. Create a user, 2. Login, 3.Connect to the chat, 4. List all registered users, 5. Exit."))
    options = {'1' , '2' , '3', '4', '5'}
    while selection not in options:
        selection = (input("Welcome to the secret chat please choose one of the following menu items by choosing the corosponding menu item and hitting enter 1. Create a user, 2. Login, 3.Connect to the chat, 4. List all registered users, 5. Exit."))
    while selection != '5':
        if selection == '1':
            userinput = input("Please, enter the username")
            while userinput in username:
                userinput = input("Username already registered, please enter another name")
            username.add(userinput)
            print("User " + userinput + " registered")
        elif selection == '4':
            for user in username:
                print(user)
        exit = input("You selected " + selection + ", press enter to go back")
        selection = (input("Welcome to the secret chat please choose one of the following menu items by choosing the corosponding menu item and hitting enter 1. Create a user, 2. Login, 3.Connect to the chat, 4. List all registered users, 5. Exit."))
    print("Thank you for using our secret chat!")
if __name__ == '__main__':
    main()