#Problem 1 for chapter 6
# Write a program to find the greatest of four numbers entered by the user. 
a1= int(input("Enter number 1: "))
a2= int(input("Enter number 2: "))
a3= int(input("Enter number 3: "))
a4= int(input("Enter number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is the greatest number among {a1},{a2},{a3} and {a4}")

if(a2>a1 and a2>a3 and a2>a4):
    print(f"{a2} is the greatest number among {a1},{a2},{a3} and {a4}")

if(a3>a1 and a3>a2 and a3>a4):
    print(f"{a3} is the greatest number among {a1},{a2},{a3} and {a4}")

else:
    print(f"{a4} is the greatest number among {a1},{a2},{a3} and {a4}")
