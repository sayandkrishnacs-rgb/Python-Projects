# Python Calculator Version 1

print("Welcome to the Calculator")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter the operator(+,-,*,/): ")

if operator=="+":
    print(num1 + num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    if num2==0:
        print("Error! Division by zero.")
    else:
        print(num1/num2)
elif operator=="%":
    if num2==0:
        print("Error! Division by zero.")
    else:
        print(num1%num2)
elif operator=="**":
    print(num1**num2)
elif operator=="//":
    print(num1//num2)
else:
    print("Invalid operator")
