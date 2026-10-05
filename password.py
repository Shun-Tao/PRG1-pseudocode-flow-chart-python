# Stored password
stored_password = "password123"

# Initialise counter
counter = 0

while True:
    # Input password
    password = input("Enter password: ")

    # Check password
    if password == stored_password:
        print("Logged in")
        break

    else:
        print("Password is wrong")
        counter = counter + 1

        # Check number of attempts
        if counter == 3:
            print("supit hakr")
            break