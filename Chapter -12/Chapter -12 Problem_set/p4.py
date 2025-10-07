# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("infinite")