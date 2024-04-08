#import mysql.connector

 

#connection = mysql.connector.connect(user = 'root', database ='bank', password = 'Katyisd#1')

 

#connection.close()

# welcome user
print("Hello, thank you for using SwiftBank! To see or adjust your bank information, please enter your account number and PIN number to get started.")
print("")

#user login
account_number = input("Please enter your 10-digit account number: ")

# validate account number digits
while len(account_number) != 10:
    account_number = input("Invalid, try again. Please enter your 10-digit account number: ")


PIN_number = input("Please enter your 4-digit PIN number: ")
while len(PIN_number) != 4:
    PIN_number = input("Invalid, try again. Please enter your 4-digit PIN number: ")

#options
print("Login Successful!")
print("")
print("")
print("***************")
print("Welcome to SwiftBank! Please select from the action options below:")

def display_options():
    print("1. Check Balance")
    print("2. Add a Deposit")
    print("3. Do a Withdraw")
    print("4. Account Settings")
    print("5. Exit SwiftBank")

display_options()
action_option = int(input("Please enter an option from 1-4: "))

#Check balance, print tables
if (action_option == 1):
    account_balance = 400
    print(f"Your current account balance is: ${account_balance}")

#deposit in account
elif (action_option == 2):
    deposit_amount = int(input("How much do you want to deposit? "))
    print("1. Bank Transfer")
    print("2. Wire Transfer")
    print("Please choose an option from 1-2: ")
    deposit_method = int(input("Please choose a deposit method: "))
    if (deposit_method == 1):
        print("Bank Transfer: ")
        confirm_account = input("Please confirm your account number to deposit funds: ")
        routing_number = input("Please confirm the routing number of the bank of the transfer:  ")
        transfer_description = input("Please enter any additional notes for the transfer: ")
        print(f"Deposit complete! You have deposited ${deposit_method} through bank transfer!")
        # display_options()
        # TO-DO: add function to display transactions
    elif (deposit_method == 2):
        print("Wire Transfer: ")
        confirm_account = input("Please confirm your account number to deposit funds: ")

elif (action_option == 3):
    print("Do a withdraw")
    withdrawal_method = int(input("Please choose a withdrawal method: "))
    print("1. Credit/Debit Card")
    print("2. Bank Transfer")
    print("3. Mobile Wallets (Apple Pay, Google Pay, Samsung Pay)")
    print("Please choose an option from 1-3: ")
    if (withdrawal_method == 1):
        debit_or_credit = input("Please enter type of card (debit or credit): ")
        card_number = int(input("Please enter card number: "))
        cardholder_name = input("Please enter the full name of the cardholder: ")
        expiration_date = input("Please enter the expiration date")
        cvc = input("Please enter the CVV/CVC: ")
    elif (withdrawal_method == 2): 
        bank_name = input("Please enter the name of the bank: ")
        recipient_holder_name = input("Please enter the account recipient's full name: ")
        recipient_account_number = input("Please enter the recipient's account number: ")

elif (action_option == 4):
    print("")
    print("************")
    print("Account settings: choose one of the following options: ")
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