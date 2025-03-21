'''Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 - 100 => Ex 
80 - 90 => A 
70 - 80 => B 
60 - 70  =>C 
50 - 60 => D 
<50     => F '''

marks = int(input("Enter you obtain mark: "))

if (marks>=90 and marks<=100):
    grade = "A+"
elif(marks>=80 and marks <= 90):
    grade = "A"
elif(marks >=70 and marks <= 80):
    grade = "B"
elif(marks >=60 and marks <= 70):
    grade = "C"
elif(marks >=50 and marks <= 60):
    grade = "D"
elif(marks<=49 and marks >=1):
    grade = "F"
elif( marks==0):
    grade = "Quite study nigga!"
    
print("Your grade is:",grade)

# marks == 0