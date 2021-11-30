print("CREATE ACCOUNT")
user = input("enter your name")
username = input("Enter your name")
password = input("Enter password")
password_confirmation = input("Re-enter your password")


option = int(input("Enter 1 to log in and 2 to exit"))
def acc_created():
# userName = input("Enter your username")
    if username != password and password_confirmation == password:
        print("Account created successfully.Click next to log in")
        global option
        option = int(input("Enter 1 to log in and 2 to exit"))
        if option == 1:
            print("WELCOME")
        else:
            print("You have exited log in menu.Try again")
    elif username != password and password_confirmation != password_confirmation:
        print("Password does not match.Try again")
    elif username == password or username == password_confirmation and password_confirmation != password:
        print("Password should not match your username and passwords entered should be the same")


acc_created()


if option == 1:
    print("Enter your details")
YourName = input("enter your name")
Password = input("Enter your password")


def acc_login():
    if YourName == username and password == password_confirmation and Password ==password_confirmation:
        print("You have successfully loged in")
    else:
        print("Wrong log in details")

