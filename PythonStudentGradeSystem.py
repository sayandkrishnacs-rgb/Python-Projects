# Student Grading System

print("=================================================")
print(".............STUDENT GRADING SYSTEM..............")
print("=================================================")

print("1. Add Student ")
print("2. View Students ")
print("3. Calculate Class Average ")
print("4. Find Highest Score ")
print("5. Find Lowest Score ")
print("6. Exit ")

names = []
marks = []


while True:
    function = input("What do you want to do?: ")
    if function.lower()=="add student":
        name = input("Enter the name of the student: ")
        names.append(name)
        
    

        mark = int(input("Enter the mark of the student: "))
        marks.append(mark)
        
        if mark>100 or mark<0:
            print("Mark cannot be lower than zero or greater then 100")
            mark = int(input("Enter the mark of the student: "))
        else:
            print(f"{name} is added to the database")
    elif function.lower()=="view students":
        print("=======================================")
        print("              DATABASE                 ")
        print("=======================================")
        print("Names             Marks")
        for name,mark in zip(names,marks):
         print(f"{name}                 {mark}/100")
    elif function.lower()=="find highest score":
        print("=======================================")

        highest_mark = max(marks)
        position = marks.index(highest_mark)
        print(f" The Highest mark is {highest_mark} scored by {name.index(position)} ")

        print("========================================")
    elif function.lower()=="find lowest score":
        print("========================================")

        lowest_score = min(marks)
        position2 = marks.index(lowest_score)
        print(f"The Lowest Mark is {lowest_score} scored by {name.index(position2)}")

        print("========================================")
    elif function.lower()=="calculate class average":
        print("========================================")

        total = sum(marks)
        char = len(marks)
        average = total/char
        print(f"The Class Average is {average}")
        print("========================================")

    elif function.lower()=="exit":
        break

        
    