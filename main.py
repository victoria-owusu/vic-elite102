import mysql.connector
from rich.console import Console
from rich.table import Table
from rich.text import Text

#create console object to change colors, etc.
console = Console()
 
# add sql connector, establish connection
connection = mysql.connector.connect(user = 'root', database = 'bank', password = 'Katyisd#1')
cursor = connection.cursor()

testQuery = ("SELECT * FROM transactions")

# create transactions table to list transactions
transactions_table = Table(show_header=True, header_style="")
transactions_table.add_column("TransactionType", style="bold", header_style="rosy_brown")
transactions_table.add_column("Amount", style="bold", header_style="rosy_brown")
transactions_table.add_column("TransactionDate", style="bold", header_style="rosy_brown")
transactions_table.add_column("TransactionName", style="bold", header_style="rosy_brown")
transactions_table.add_column("Status", style="bold", header_style="rosy_brown")
transactions_table.add_column("PaymentMethod", style="bold", header_style="rosy_brown")
cursor.execute(testQuery)
rows = cursor.fetchall()

# change account menu
change_menu = Table(show_header=True, header_style = "")
change_menu.add_column("Number", style="italic white", header_style="bold")
change_menu.add_column("Option", style="blue", header_style="bold")


change_menu.add_row("1", "Change email")
change_menu.add_row("2", "Change password")
change_menu.add_row("3", "Change username")

# welcome user
account_balance = 400
print("")
console.print("\nHello, thank you for using SwiftBank! To see or adjust your bank information, please enter your account number and PIN number to get started.\n", style="bold purple")
print("")

#user login
console.print("Please enter your [underline][italic]10-digit [/italic][/underline]account number:")
account_number = input("")

# validate account number digits
while len(account_number) != 10:
    console.print("\nInvalid, try again. Please enter your 10-digit account number: ", style="italic red")
    account_number = input("")

#validate pin number
console.print("\nPlease enter your [underline][italic]4-digit[/underline][/italic] PIN number: ")
PIN_number = input("")
while len(PIN_number) != 4:
    console.print("\nInvalid, try again. Please enter your 4-digit PIN number: ", style="italic red")
    PIN_number = input("")

#create account list
#created dictionary with each representing an ccount iwht three key-value pairs
account_list = [
{"username": "default", "password": "default", "email": "default@gmail.com" }
]

#list accounts into table
account_table = Table(show_header=True, header_style="")
account_table.add_column("Number", style="bold", header_style="light_slate_blue")
account_table.add_column("Account Name", style="bold", header_style="light_slate_blue")




#options
console.print("Login Successful!", style="italic green")
print("")
print("")
#welcome to swiftbank
print("***************")
console.print("Welcome to SwiftBank! Please select from the action options below:", style=" italic purple")
print("")

#displayed main-menu on a table for user to choose where they want to go
def display_options():
    main_menu = Table(show_header=True, header_style = "")
    main_menu.add_column("Number", style="italic white", header_style="bold")
    main_menu.add_column("Option", style="blue", header_style="bold")

    main_menu.add_row("1", "Check Balance")
    main_menu.add_row("2", "Add a Deposit")
    main_menu.add_row("3","Do a Withdrawal")
    main_menu.add_row("4", "Account Settings")
    main_menu.add_row("5", "Exit SwiftBank")
    console.print(main_menu)

display_options()

# add deposit function
def make_deposit(amount, method, balance):
   
    if (deposit_method == 1):
        #allow user to choose bank transfer
        print("***************")
        console.print("\nBank Transfer: ", style="italic violet")
        confirm_account = input("Please confirm your account number to deposit funds: ")
        routing_number = input("Please confirm the routing number of the bank of the transfer:  ")
        transfer_description = input("Please enter any additional notes for the transfer: ")
        console.print(f"\nDeposit complete! You have deposited ${deposit_amount} through bank transfer!", style="italic green")
        
        #add deposit into transactions data
        addData = ("INSERT INTO transactions (TransactionType, Amount, TransactionDate, TransactionName, Status, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s)")
        transaction_data = ('Deposit', deposit_amount, '2024-04-24', 'Bank Transfer 1', 'Completed', 'Bank Transfer')
        
        

    elif (deposit_method == 2):
        #allow user to choose wire transfer
        console.print("\nWire Transfer: ", style="italic violet")
        confirm_account = input("Please confirm your account number to deposit funds: ")
        bank_name = input("Please enter your bank's name: ")
        routing_number = input("Enter your bank's routing number: ")
        print("")
        console.print(f"Deposit complete! You have deposited ${deposit_amount} through wire transfer!", style="italic green")
        
        #add deposit into transactions data
        addData = ("INSERT INTO transactions (TransactionType, Amount, TransactionDate, TransactionName, Status, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s)")
        transaction_data = ('Deposit', deposit_amount, '2024-04-24', 'Wire Transfer 1', 'Completed', 'Wire Transfer')
    
    cursor.execute(addData, transaction_data)

        # Commit the transaction
    connection.commit()

    #add deposit to balance
    balance = account_balance
    balance = balance + deposit_amount
    print(f"Your current account balance is: ${balance}")
    console.print("Transaction data added successfully!", style="italic green")
    print("")
    
   
    
    

#make withdrawal function
def make_withdrawal(amount, method, balance):
     
      #credit or debit card
      if (withdrawal_method == 1):
        print("")
        debit_or_credit = input("Please enter type of card (debit or credit): ")
        card_number = int(input("Please enter card number: "))
        cardholder_name = input("Please enter the full name of the cardholder: ")
        expiration_date = input("Please enter the expiration date: ")
        cvc = input("Please enter the CVV/CVC: ")
        print("")
        console.print(f"Withdrawal complete! You have withdrew ${withdrawal_amount} through {debit_or_credit} card!", style="italic green")
       
        # add withdrawal transaction data
        addData = ("INSERT INTO transactions (TransactionType, Amount, TransactionDate, TransactionName, Status, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s)")
        transaction_data = ('Withdrawal', withdrawal_amount, '2024-04-24', 'Credit/Debit Withdrawal', 'Completed', 'Credit/Debit Card')
       
        #bank transfer
      elif (withdrawal_method == 2): 
        print("")
        bank_name = input("Please enter the name of the bank: ")
        recipient_holder_name = input("Please enter the account recipient's full name: ")
        recipient_account_number = input("Please enter the recipient's account number: ")
        recipient_routing_number = input("Please enter the recipient's routing number: ")
        transfer_reference = input("Please enter any additional info for the transfer: ")
        print("")
        console.print(f"Withdrawal complete! You have withdrew ${withdrawal_amount} through bank transfer to ${recipient_holder_name}!", style="italic green")
       
        # add withdrawal transaction data
        addData = ("INSERT INTO transactions (TransactionType, Amount, TransactionDate, TransactionName, Status, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s)")
        transaction_data = ('Withdrawal', withdrawal_amount, '2024-04-24', 'Bank Transfer Withdrawal', 'Completed', 'Bank Transfer')

        
        #mobile wallet
      elif (withdrawal_method == 3):
        print("")
        mobile_wallet_provider = input("Please enter the mobile wallet provider you'll be using: ")
        user_id = input("Please enter your user id: ")
        phone_number = input("Please enter your phone number (XXX-XXX-XXXX): ")
        mobile_wallet_password = input("Please enter your password used for mobile wallet: ")
        mobile_wallet_note = input("Please enter any additional notes for this withdrawal: ")
        print("")
        console.print(f"Withdrawal complete! You have withdrew ${withdrawal_amount} through your mobile wallet!", style="italic green")
        
        #add withdrawal transaction data
        addData = ("INSERT INTO transactions (TransactionType, Amount, TransactionDate, TransactionName, Status, PaymentMethod) VALUES (%s, %s, %s, %s, %s, %s)")
        transaction_data = ('Withdrawal', withdrawal_amount, '2024-04-24', 'Mobile Wallet Withdrawal', 'Completed', 'Mobile Wallet')
      
      cursor.execute(addData, transaction_data)

        # Commit the transaction
      connection.commit()

      # add withdrawal into balance
      balance = account_balance
      balance = balance - withdrawal_amount 
      print(f"Your current account balance is: ${balance}") 
      console.print("Transaction data added successfully!", style="italic green")
      print("")

def create_account(user, password, email):
    # everytime account is created
    new_account = {"username": user, "email": email, "password": password}
    #add account into list
    account_list.append(new_account)
    console.print(f"Welcome {user}, your account has been created!", style="italic green")
    #display current accounts
    for data in account_list:
            account_table.add_row(
                str(data.get("username", "")),
                str(data.get("email", "")),
                str(data.get("password", "")),
            )

          
def delete_account(account, acc_number, pin):
   #warning to user
   if len(account_list) == 1:
       console.print("You cannot delete the **default** account. Only additionally made accounts can be deleted.", style="italic red")
       return
   
   # deleting accounts
   acccount =  input("What account do you want to delete besides default? ")
   for account in account_list:
        if account["username"] == account:
            console.print(f"Starting process to delete ${account}.", style="italic")
   acc_number = account_number
   pin = PIN_number

   #validation
   confirm_acc_number = input("Please confirm your account number: ")
   while confirm_acc_number != account_number:
       console.print("Please try again, incorrect account number: ", style="italic red")
       confirm_acc_number = input("")
   confirm_pin = input("Please confirm your pin number: ")
   while confirm_pin != PIN_number:
       console.print("Please try again, incorrect pin number: ", style="italic red")
       confirm_pin = input("")
   print("Deleting account....")
   account_list.pop(1)
   print("Account Deleted!")
   #show account list
   for data in account_list:
            account_table.add_row(
                str(data.get("username", "")),
                str(data.get("password", "")),
                str(data.get("email", "")),
            )
   console.print(f"\nCurrent Accounts: ", style="bold purple")
   console.print(account_list)

   
  

def change_email(username, new_email):
  #for loop is used to find dictionar ycorresponding to specified username
  for account in account_list:
        if account["username"] == username:
            account["email"] = new_email
            console.print(f"Email address has been updated successfully to {new_email}", style="italic green")
            break
  else:
        #notify user username is not found
        console.print("Username not found.", style="italic red")


def change_password(username, new_password):
       #for loop is used to find dictionar ycorresponding to specified username
     for account in account_list:
        if account["username"] == username:
            account["password"] = new_password
            console.print(f"Password has been updated successfully to {new_password}", style="italic red")
            break
     else:
        console.print("Password not found.", style="italic red")

def change_user(username, new_username):
      #for loop is used to find dictionar ycorresponding to specified username
    for account in account_list:
        if account["username"] == username:
            account["username"] = new_username
            console.print(f"The Username has been updated successfully to {new_username}", style="italic green")
            break
    else:
        console.print("Password not found.", style="italic red")

#allow user to choose option from main menu
console.print("\nPlease enter an option from 1-5: ", style="blue")
action_option = int(input(""))

#Check balance, print tables
if (action_option == 1):
    print("")
    
    #display current account balance
    console.print(f"[underline]Your current account balance is:[/underline] ${account_balance}",style="dim")
    print("\n*************")
    
    #display past transactions
    console.print("Here is the list of your past transactions: ", style="bold dark_magenta")
    
    #print transactions table
    for row in rows:
        transactions_table.add_row(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
    console.print(transactions_table)

#deposit in account
elif (action_option == 2):
    console.print("How much do you want to deposit?", style="bold")

    #display deposit options in a table
    deposit_amount = int(input(""))
    deposit_menu = Table(show_header=True, header_style = "")
    deposit_menu.add_column("Number", style="italic white", header_style="bold")
    deposit_menu.add_column("Option", style="blue", header_style="bold")

    deposit_menu.add_row("1", "Bank Transfer")
    deposit_menu.add_row("2", "Wire Transfer")

    print("")
    console.print(deposit_menu)
    print("Please choose an option from 1-2 ")
    deposit_method = int(input("Please choose a deposit method: "))
    
    #user makes deposit
    make_deposit(deposit_amount, deposit_method, account_balance)
    
    #print transactions table
    print("Here is the list of your past transactions: ")
    for row in rows:
        transactions_table.add_row(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
    console.print(transactions_table)
   
    
   
    
   
#make a withdrawal
elif (action_option == 3):
    # input withdrawal amount
    print("")
    console.print("Please enter the amount you would like to withdrawal:", style="bold")
    withdrawal_amount = int(input(" "))


    #display withdrawal options with table
    withdrawal_menu = Table(show_header=True, header_style="")
    withdrawal_menu.add_column("Number", style="italic white", header_style="bold")
    withdrawal_menu.add_column("Option", style="blue", header_style="bold")


    withdrawal_menu.add_row("1", "Credit/Debit Card")
    withdrawal_menu.add_row("2", "Bank Transfer")
    withdrawal_menu.add_row("3", "Mobile Wallets (Apple Pay, Google Pay, Samsung Pay)" )

    console.print(withdrawal_amount)
    console.print("Please choose a withdrawal method from 1-3: ", style="bold")
    withdrawal_method = int(input(""))
    make_withdrawal(withdrawal_amount, withdrawal_method, account_balance)
    

# account settings
elif (action_option == 4):
    print("")
    print("************")
    console.print("Account settings: choose one of the following options: ", style="bold plum4")
    account_settings = Table(show_header=True, header_style="")

    #display account setting options with table
    account_settings.add_column("Number", style="italic white", header_style="bold")
    account_settings.add_column("Option", style="blue", header_style="bold")

    account_settings.add_row("1", "Create a new account")
    account_settings.add_row("2", "Close account")
    account_settings.add_row("3", "Modify an account")
    account_settings.add_row("4", "Exit SwiftBank")
    console.print(account_settings)

    print("")
    console.print("\nPlease enter an option from 1-3: ", style="bold")
    admin_option = int(input(""))

#edit account
    if (admin_option == 1):
        new_user = input("Please enter new username: ")  
        new_pass = input("Please enter new password: ")
        confirm_pass = input("Please confirm password: ")
        while new_pass != confirm_pass:
            console.print("\nIncorrect, please use the correct password: ", style="italic red")
            confirm_pass = input(" ")
        email_address = input("Please enter your email address: ")
        confirm_email = input("Please confirm your email address: ")
        while email_address != confirm_email:
            console.print("\nIncorrect, please use the correct email address: ", style="italic red")
            confirm_email = input("")
        create_account(new_user, new_pass, email_address)
        print("")

        #display current accounts
        for data in account_list:
            account_table.add_row(
                str(data.get("username", "")),
                str(data.get("password", "")),
                str(data.get("email", "")),
            )
        console.print(f"\nCurrent Accounts: ", style="bold purple")
        console.print(account_list)

        #allow user to delete new account
        print("******************")
        console.print("\nDo you want to delete this account? 1 for yes, 2 for no ", style="bold red")
        deletion = int(input(""))
        if (deletion == 1):
            delete_account(new_user, account_number, PIN_number)
        elif (deletion == 2):
            print("Okay, thank you for using SwiftBank!", style="bold purple")

        
    
    elif (admin_option == 2):
        #restrict user from deleting default account
        console.print("\nNotice: You are not allowed to delete your default account, which only account number and PIN are only required.", style="bold red")
        delete_account('default', account_number, PIN_number)
        print("")
        console.print("\nRun program again to start over.", style="bold red")
        exit()
   
    #modify account information
    elif (admin_option == 3):
        for data in account_list:
            account_table.add_row(
                str(data.get("username", "")),
                str(data.get("password", "")),
                str(data.get("email", "")),
            )

        #display current 
        console.print(f"\nCurrent Accounts: ", style="bold purple")
        print("")
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
           
            print("")
            console.print(change_menu)
        else:
            console.print("\nInvalid account, try again.", style="italic red")
            
            while not verify_account_existence(account_to_modify):
                account_to_modify = input("What account would you like to change? Please enter the username of an account: ")
                verify_account_existence(account_to_modify)
            print("")
            console.print(change_menu)
        
        #allow user to choose waht they would like to change
        modify_option = int(input("Please choose from 1-3: "))

        #change email
        if (modify_option == 1):
            new_email = input("Please enter your changed email address: ")
            change_email(account_to_modify, new_email)
        
        #change password
        elif (modify_option == 2):
            new_password = input("Please enter your changed password: ")
            change_password(account_to_modify, new_password)

        #change username
        elif(modify_option == 3):
            new_user = input("Please enter your changed username: ")
            change_user(account_to_modify, new_user)


        
        
        
    #thank user
    elif (admin_option == 4):
        console.print("Thank you for using SwiftBank!", style="italic green")
        exit()
    else: 
        console.print("Invalid response response, please try again.", style="italic red")
        admin_option = int(input("\nPlease enter an option from 1-3: "))

#thank user, immediately exit program
elif (action_option == 5):
    console.print("Thank you for using SwiftBank!", style="italic green")
    exit()

else: 
    console.print("Invalid response response, please try again.", style="italic red")
    action_option = int(input("Please enter an option from 1-4: "))

#close connection with sqlconnector
cursor.close()

connection.close()
