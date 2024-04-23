#import mysql.connector
import tkinter
import unittest

 

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

#create account list
#created dictionary with each representing an ccount iwht three key-value pairs
account_list = [
{"username": "default", "password": "default", "email": "default@gmail.com" }
]
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
    print("")

display_options()

# add deposit function
def make_deposit(amount, method):
    if (deposit_method == 1):
        print("Bank Transfer: ")
        confirm_account = input("Please confirm your account number to deposit funds: ")
        routing_number = input("Please confirm the routing number of the bank of the transfer:  ")
        transfer_description = input("Please enter any additional notes for the transfer: ")
        print(f"Deposit complete! You have deposited ${deposit_amount} through bank transfer!")
        # display_options()
        # TO-DO: add function to display transactions
    elif (deposit_method == 2):
        print("Wire Transfer: ")
        confirm_account = input("Please confirm your account number to deposit funds: ")
        bank_name = input("Please enter your bank's name: ")
        routing_number = input("Enter your bank's routing number: ")
        print("")
        print(f"Deposit complete! You have deposited ${deposit_amount} through wire transfer!")

#make withdrawal function
def make_withdrawal(amount, method):
     
      #credit or debit card
      if (withdrawal_method == 1):
        debit_or_credit = input("Please enter type of card (debit or credit): ")
        card_number = int(input("Please enter card number: "))
        cardholder_name = input("Please enter the full name of the cardholder: ")
        expiration_date = input("Please enter the expiration date")
        cvc = input("Please enter the CVV/CVC: ")
        print(f"Withdrawal complete! You have withdrew ${withdrawal_amount} through ${debit_or_credit} card!")
       
        #bank transfer
      elif (withdrawal_method == 2): 
        bank_name = input("Please enter the name of the bank: ")
        recipient_holder_name = input("Please enter the account recipient's full name: ")
        recipient_account_number = input("Please enter the recipient's account number: ")
        recipient_routing_number = input("Please enter the recipient's routing number: ")
        transfer_reference = input("Please enter any additional info for the transfer: ")
        print(f"Withdrawal complete! You have withdrew ${withdrawal_amount} through bank transfer to ${recipient_holder_name}!")
        
        #mobile wallet
      elif (withdrawal_method == 3):
        mobile_wallet_provider = input("Please enter the mobile wallet provider you'll be using: ")
        user_id = input("Please enter your user id: ")
        phone_number = input("Please enter your phone number (XXX-XXX-XXXX): ")
        mobile_wallet_password = input("Please enter your password used for mobile wallet: ")
        mobile_wallet_note = input("Please enter any additional notes for this withdrawal: ")
        print(f"Withdrawal complete! You have withdrew ${withdrawal_amount} through your mobile wallet!")

def create_account(user, password, email):
    # everytime account is created
    new_account = {"username": user, "email": email, "password": password}
    account_list.append(new_account)
    print(f"Welcome {user}, your account has been created!")

          
def delete_account(account, acc_number, pin):
   if len(account_list) == 1 and account_list[0] == 'default':
       print("You cannot delete the **default** account. Only additionally made accounts can be deleted.")
       return
   acccount =  input("What account do you want to delete besides default? ")
   for account in account_list:
        if account["username"] == account:
            print(f"Starting process to delete ${account}.")
   acc_number = account_number
   pin = PIN_number
   confirm_acc_number = input("Please confirm your account number: ")
   while confirm_acc_number != account_number:
       confirm_acc_number = input("Please try again, incorrect account number: ")
   confirm_pin = input("Please confirm your pin number: ")
   while confirm_pin != PIN_number:
       confirm_pin = input("Please try again, incorrect account number: ")
   print("Deleting account....")
   account_list.pop(1)
   print("Account Deleted!")
   print(f"Current Accounts: ${account_list}")
  

def change_email(username, new_email):
  #for loop is used to find dictionar ycorresponding to specified username
  for account in account_list:
        if account["username"] == username:
            account["email"] = new_email
            print(f"Email address has been updated successfully to {new_email}")
            break
  else:
        print("Username not found.")

def change_password(username, new_password):
     for account in account_list:
        if account["username"] == username:
            account["password"] = new_password
            print(f"Password has been updated successfully to {new_password}")
            break
     else:
        print("Password not found.")

def change_user(username, new_username):
    for account in account_list:
        if account["username"] == username:
            account["username"] = new_username
            print(f"The Uuername has been updated successfully to {new_username}")
            break
    else:
        print("Password not found.")

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
    print("")
    print("Please choose an option from 1-2 ")
    deposit_method = int(input("Please choose a deposit method: "))
    make_deposit(deposit_amount, deposit_method)
   
    
   
#make a withdrawal
elif (action_option == 3):
    print("Do a withdraw")
    print("")
    withdrawal_amount = int(input("Please enter the amount you would like to withdrawal: "))
    print("1. Credit/Debit Card")
    print("2. Bank Transfer")
    print("3. Mobile Wallets (Apple Pay, Google Pay, Samsung Pay)")
    withdrawal_method = int(input("Please choose a withdrawal method from 1-3: "))
    make_withdrawal(withdrawal_amount, withdrawal_method)
    

# account settings
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
        new_user = input("Please enter new username: ")  
        new_pass = input("Please enter new password: ")
        confirm_pass = input("Please confirm password: ")
        while new_pass != confirm_pass:
            confirm_pass = input("Incorrect, please use the correct password: ")
        email_address = input("Please enter your email address: ")
        confirm_email = input("Please confirm your email address: ")
        while email_address != confirm_email:
            confirm_email = input("Incorrect, please use the correct email address: ")
        create_account(new_user, new_pass, email_address)
        print(f"Current Accounts: {account_list}")
        deletion = int(input("Do you want to delete this account? 1 for yes, 2 for no "))
        if (deletion == 1):
            delete_account(new_user, account_number, PIN_number)
        elif (deletion == 2):
            print("Okay, thank you for using SwiftBank!")

        
    
    elif (admin_option == 2):
        print("Notice: You are not allowed to delete your default account, which only account number and PIN are only required.")
        delete_account()
        print("")
        print("Run program again to start over.")
        exit()
   
    #modify account information
    elif (admin_option == 3):
        print(f"Current Accounts: {account_list}")
        account_to_modify = input("What account would you like to change? Please enter the username of an account: ")
         # Check if the entered username exists in any of the dictionaries in account_list
        def verify_account_existence(account):
            username_exists = False
            for account in account_list:
                if account['username'] == account_to_modify:
                    username_exists = True
                    return username_exists
                    break
        verify_account_existence(account_to_modify)
        # continuously ask the user to keep submitting until a valid response is inputted
        if verify_account_existence(account_to_modify):
            print("1. Change email")
            print("2. Change password")
            print("3. Change username")
        else:
            print("Invalid account, try again.")
            while not verify_account_existence(account_to_modify):
                account_to_modify = input("What account would you like to change? Please enter the username of an account: ")
                verify_account_existence(account_to_modify)
            print("1. Change email")
            print("2. Change password")
            print("3. Change username")
        
        #allow user to choose waht they would like to change
        modify_option = int(input("Please choose from 1-3: "))
        if (modify_option == 1):
            new_email = input("Please enter your changed email address: ")
            change_email(account_to_modify, new_email)
        
        elif (modify_option == 2):
            new_password = input("Please enter your changed password: ")
            change_password(account_to_modify, new_password)

        elif(modify_option == 3):
            new_user = input("Please enter your changed username: ")
            change_user(account_to_modify, new_user)


        
        
        

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