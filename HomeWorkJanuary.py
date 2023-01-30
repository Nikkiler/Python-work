def main():
    username = input("Welcome to our new messenger! How can I call you?")
    answer = input("Hello, " + username + "! Do you want to say something?")
    answer = answer.lower()
    while answer != "yes" and answer != "no":
        print("Please, answer only yes or no")
        answer = input("Hello, " + username + "! Do you want to say something?")
        answer = answer.lower()
    while answer != "no":
        say = input("What do you want to say? ")
        print(username + ': ' + say)
        answer = input("Hello, " + username + "! Do you want to say something?")
        answer = answer.lower()
        while answer != "yes" and answer != "no":
            print("Please, answer only yes or no")
            answer = input("Hello, " + username + "! Do you want to say something?")
            answer = answer.lower()
    l = input("Press Enter To Exit")
if __name__ == '__main__':
    main()