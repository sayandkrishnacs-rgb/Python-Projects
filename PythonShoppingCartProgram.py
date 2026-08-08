# Shopping cart Program


foods = []
prices = []
Total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food == "q" or food == "Q":
        break
    else:
        price = float(input("Enter the price of the food:$ "))
        foods.append(food)
        prices.append(price)

print("-------- YOUR CART --------")

for food in foods:
    print(food)

for price in prices:
    print("$", price)

print("\n.............................")

total = sum(prices)
print(f"Total: $ {total:.2f}")