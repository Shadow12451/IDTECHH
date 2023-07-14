guessed = False


while not guessed:
    password = input("Enter a password: ")
    if password == "PythonCoding":
        guessed = True
        print("Access Granted!")
    else:
        print("Access denied! Try again.")