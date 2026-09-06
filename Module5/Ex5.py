tries = 0

while tries < 5:
    username = input("Username: ")
    password = input("Password: ")

    if username == "python" and password == "rules":
        print("Welcome")
        break

    tries = tries + 1
else:
    print("Access denied")