def main():
    username = set()
    menu()
    selection = (input(""))
    options = {'1' , '2' , '3', '4', '5'}
    while selection not in options:
        menu()
        selection = (input(""))
    while selection != '5':
        if selection == '1':
            option1(username)
        elif selection == '4':
            option4(username)
            menu()
        selection = (input(""))
    print("Thank you for using our secret chat!")
def option1(username):
    userinput = input("Please, enter the username")
    while len(userinput) == 0:
        userinput = input("Username is null please enter another name, please enter another name")
    while userinput in username:
        userinput = input("Username already registered, please enter another name")
        while len(userinput) == 0:
            userinput = input("Username is null please enter another name, please enter another name")
    username.add(userinput)
    print("User " + userinput + " registered")
def option4(username):
    for user in username:
        print(user)
def menu():
    print("please choose one of the following menu items")
    print("by choosing the corosponding menu item and hitting enter")
    print("1. Create a user")
    print("2. Login")
    print("3. Connect to the chat")
    print("4. List all registered users")
    print("5. Exit.")
if __name__ == '__main__':
    main()