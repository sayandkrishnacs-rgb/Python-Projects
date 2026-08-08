# Python Cocession Stand Program

print("================================")
print("       CONCESSION STAND         ")
print("================================")

options = {"0":"Popcorn",
           "1":"Soda",
           "2":"Hotdog",
           "3":"Nachos",
           "4":"Candy",
           "5":"Water",
         "6":"Checkout"}


Items = {"0":"Popcorn   $5.00",
         "1":"Soda      $3.00",
         "2":"Hotdog    $4.00",
         "3":"Nachos    $6.00",
         "4":"Candy     $2.00",
         "5":"Water     $1.00",
         "6":"Checkout"}

for item in Items:
    print(f"{item}: {Items[item]}")

Qum = []
pri = []

prices = {"0":5.00,
          "1":3.00,
          "2":4.00,
          "3":6.00,
          "4":2.00,
          "5":1.00  }


while True:
    choice = input("Please enter the number of the item you want: ")
    


    if choice == "6":
     print("Thank you for your purchase!")

     print("================================")
     print("   CONCESSION STAND RECEIPT")
     print("================================")

     total = 0
     for a, b in zip(Qum, pri):
       total += a*b
     print(f"Total: ${total:.2f}")


     payment = float(input("Please enter your payment amount: $"))
 
     if payment == total:
        print("Payment accepted. Thank you!")
        break
     elif payment > total:
         change = payment - total
         print(f"Payment accepted. Your change is ${change:.2f}. Thank you!")
     else:
        print("Insufficient payment. Please try again.")
     break
            
    
        

    
    Quantity = int(input("How many would you like?: "))
    Qum.append(Quantity)
    pri.append(prices[choice])
    print(f"Added {Quantity} {options[choice]} to your cart.")
    
