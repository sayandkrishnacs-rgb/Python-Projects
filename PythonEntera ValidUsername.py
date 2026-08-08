# validate user input excercise
# 1. username is no more than 12 characters 
# 2. username must not contain spaces
# 3.username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("The username should be no more than 12 characters")
elif not username.find(" ")==-1:
    print("The username must not contain any spaces")
elif username.isdigit():
    print("The username must not contain any digits" )
else:
    print(f"Your username is now set as:{username}")
