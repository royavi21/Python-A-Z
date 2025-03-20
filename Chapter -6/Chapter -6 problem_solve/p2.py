#This is problem number 2. Lets solve this.

# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

marks1 =int(input("Marks is English: "))
marks2 =int(input("Marks is Math: "))
marks3 =int(input("Marks is Science: "))
#check for ttotal parcentage (40%) and at least 33% in each subject

total_parcentage = (100*(marks1 + marks2 + marks3))/300

if(total_parcentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed", total_parcentage)
else:
    print("You'r failed. Better luck next time nigga!", total_parcentage)

