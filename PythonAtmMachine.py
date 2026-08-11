# Python ATM Machine Interface
while True:
 print("==============================================")
 print("................ATM MACHINE...................")
 print("==============================================")
 accounts = {"Aneesh": 454588,
             "Sam":354588}
 balance = {"Aneesh": 500,
            "Sam": 1000}
 transactions_to = []
 transactions_am = []

 username = input("Please Enter your Username:")
 password = int(input("Enter your 6 digit Pin:"))
 if accounts.get(username):
    user = accounts.get(username)
    
    if password == user:
      print("============================================")
      print(f"WELCOME {username}, ")
      print("============================================")
      print("1. Check Balance")
      print("2. Deposit Money")
      print("3. Withdraw Money")
      print("4. Transfer Money")
      print("5. Transaction History")
      print("6. Change PIN")
      print("7. Exit")

      while True:
       function = input("Enter The number to Perform the function: ")
       if function == "1":
         print("========================================")
         print(f"YOUR BALANCE IS ${balance.get(username)}")
         print("========================================")
       if function == "2":
         deposit = int(input("Enter the amount of money to be deposited:$"))
         initial = balance.get(username)+deposit
         balance.update({username: initial})
         print("===========================================")
         print(f"${deposit} HAS BEEN ADDED TO YOUR ACCOUNT")
         print(f"        NEW BALANCE: ${initial}")
         print("===========================================")
       if function =="3":
         withdraw = int(input("Enter the amount of money to be Withdrawn:$"))
         initial2 = balance.get(username)-withdraw
         balance.update({username: initial2})
         print("==================================================")
         print(f"${withdraw} HAS BEEN WITHDRAWN FROM YOUR ACCOUNT ")
         print(f"        NEW BALANCE:${initial2}                  ")
         print("         PLEASE COLLECT YOUR MONEY                ")
         print("==================================================")
       if function =="4":
         print("===================================================")
         print("                  TRANSFER                         ")

         print("===================================================")
         while True:
          transfer_amount = int(input("Enter the Amount to be Transfered:$"))
          transfer_to = input("Enter the account to want to transfer to: ")
         

          if accounts.get(transfer_to):
            reduction = balance.get(username)-transfer_amount
            balance.update({username: reduction })
            addition = balance.get(transfer_to)+transfer_amount
            balance.update({transfer_to: addition})
            transactions_to.append(transfer_to)
            transactions_am.append(transfer_amount)
            print("====================================================")
            print(f"${transfer_amount} HAS BEEN TRANSFERED FROM YOUR   ")
            print(f"      {username} TO {transfer_to}            ")
            print("====================================================")
            break
          else:
            print("ACCOUNT NOT FOUND!!")
       if function =="5":
         print("========================================================")
         print("              TRANSACTION HISTORY                       ")
         print("========================================================")
         for account,amount in zip(transactions_to,transactions_am):
           print("TO               AMOUNT")
           print(f"{account}        {amount}")
       if function == "6":
         New_pin = int(input("Enter your new PIN: "))
         old_pin = int(input("Enter your old PIN: "))
         if old_pin==accounts.get(username):
           accounts.update({username: New_pin})
       if function =="7":
         break
         
       else:
        print("NOT A VALID FUNCTION")
          
         

           
           
           
          


      
      







      break
    else:
     print("Incorrect Password")
     break

 else:
   print("Invalid Username:")
   break




