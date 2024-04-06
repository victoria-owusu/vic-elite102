# welcome user
print("Hello, thank you for using SwiftBank! To see or adjust your bank information, please enter your account number and PIN number.")
print("")

#user login
account_number = input("Please enter your account number: ")
PIN_number = input("Please enter your PIN number: ")

#options
print("Login Successful!")
print("")
print("")
print("***************")
print("Welcome to SwiftBank! Please select from the action options below:")
print("1. Check Balance")
print("2. Add a Deposit")
print("3. Do a Withdraw")
print("4. I am a new user or a bank administrator.")
print("5. Exit SwiftBank")

action_option = int(input("Please enter an option from 1-4: "))

if (action_option == 1):
    print("Balance checked.")

elif (action_option == 2):
    print("Added Deposit.")

elif (action_option == 3):
    print("Do a withdraw")

elif (action_option == 4):
    print("")
    print("************")
    print("New users and bank adminstrators, choose one of the following options: ")
    print("1. Create a new account")
    print("2. Close account")
    print("3. Modify an account")
    print("4. Exit SwiftBank")
    admin_option = int(input("Please enter an option from 1-3: "))
#edit account
    if (admin_option == 1):
        print("Account created.")
    
    elif (admin_option == 2):
        print("Account closed.")

    elif (admin_option == 3):
        print("Account modified.")

    elif (admin_option == 4):
        print("Thank you for using SwiftBank!")
        exit()
    else: 
        print("Invalid response response, please try again.")
        admin_option = int(input("Please enter an option from 1-3: "))

elif (action_option == 5):
    print("Thank you for using SwiftBank!")
    exit()

else: 
    print("Invalid response response, please try again.")
    action_option = int(input("Please enter an option from 1-4: "))