#program to validate menu choice between 1 and 5
print("Please enter your choice(1-5): ")
validChoice = "false"
count = 0
while (validChoice == "false") and (count < 3):
    choice = input()
    count = count + 1
    if choice < "1" or choice > "5":
        print("Invalid choice - must be between 1 and 5")
    else:
        validChoice = "true"
        
if validChoice == "false":
    print ("Program ending")
else:
    print("continue")