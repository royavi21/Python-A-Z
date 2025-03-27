# Function of while loops:

'''
Syntax:
while (condition): # The block keeps executing until the condition is true
#Body of the loop
In while loops, the condition is checked first. If it evaluates to true, the body of the loop
is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until
the condition becomes False.

Note:  If the condition never become false, the loop keeps getting executed.
'''

#This will print "Avijit" 5 times
i=0
while i<5:
    print("Avijit")
    i +=1

# Quick Quiz: Write a program to print 1 to 50 using a while loop.
i=0
while i<50:
    print(i+1)
    i +=1
#This will make same o/p
i=1
while i<51:
    print(i)
    i +=1

#This is some use case of while loop

print("While loop example")

