#Lets go - - fro loop

for i in range (1,6):
    print(i)

'''
A for loop is used to iterate through a sequence like list, tuple, or string [iterables] 
Syntax: 
l = [1, 7, 8] 
for item in l: 
print(item) # prints 1, 7 and 8 
RANGE FUNCTION IN PYTHON 
The range() function in python is used to generate a sequence of number. 
We can also specify the start, stop and step-size as follows: 
range(start, stop, step_size) 
# step_size is usually not used with range() 
AN EXAMPLE DEMONSTRATING RANGE () FUNCTION. 
for i in range(0,7): # range(7) can also be used. 
print(i) # prints 0 to 6 
FOR LOOP WITH ELSE 
An optional else can be used with a for loop if the code is to be executed when the 
loops exhausts. 
Example: 
l= [1,7,8] 
for item in l: 
print(item) 
else: 
print("done") # this is printed when the loop exhausts! 
Output: 
1 
7 
8 
done
'''

#Slysing
for i in range (0,21,2):
    print(i)