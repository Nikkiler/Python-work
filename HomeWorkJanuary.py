username = input("Welcome to our new messenger! How can I call you?")
answer = input("Hello, " + username + "! Do you want to say something?")
answer = answer.lower()
while answer != "no":
    say = input("What do you want to say? ")
    print(username + ': ' + say)
    answer = input("Hello, " + username + "! Do you want to say something?")
l = input("Press Any Key To Exit")