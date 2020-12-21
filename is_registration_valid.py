name = input("Enter your username: ")
if("@" in name and "." in name):
    password = input("Enter your password: ")
    if("#" in password and len(password)>=8):
        print("Congratulations! You did it!")
    else:
        print("Invalid Password")
else:
    print("Invalid Username")