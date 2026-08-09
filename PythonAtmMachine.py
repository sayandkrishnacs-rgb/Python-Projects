# Python ATM Machine Interface
while True:
 print("==============================================")
 print("................ATM MACHINE...................")
 print("==============================================")
 accounts = {"Aneesh": 454588,
             "Sam":354588}
 balance = {"Aneesh": 500,
            "Sam": 1000}

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
         print(f"YOUR BALANCE IS {balance.get(username)}")
         print("========================================")
       if function 
         

      
      







      break
    else:
     print("Incorrect Password")
     break

 else:
   print("Invalid Username:")
   break




