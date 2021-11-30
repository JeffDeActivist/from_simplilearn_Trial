username = input("Enter your username")
password = input("Enter your password")


def password_strength():
    if password == username:
        print("Password should not match username")
        if len(password) < 10:
            print("Password too short")
    elif len(password) < 10:
        print("password strength is poor")
    elif len(password) >= 10 and username != password:
        print("Password is strong.Your account is now safe")


password_strength()
