# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    return inches * 2.54
n = int(input("Enter the number of inches: "))
print(inches_to_cms(n))