#password verification
match = False
while match == False:
    print("Please enter new password: ")
    password1 = input()
    print("Please enter password again: ")
    password2 = input()
    if password1 == password2:
        match = True
        print("Please continue")
    else:
        print ("Incorrect password - please re-enter a new password: ")