import time

my_time = input("Enter the time in seconds: ")

while my_time<="0" or my_time=="":
    print("Please enter a positive number")
    my_time =input("Enter the time in seconds: ")

my_time = int(my_time)

for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = x // 60
    hour = minutes // 60
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("Times up")