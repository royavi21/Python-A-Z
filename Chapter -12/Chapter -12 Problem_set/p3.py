# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
print(table)

"""
op:
Enter a number: 7 
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

"""
