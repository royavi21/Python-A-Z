# Write a python function to print multiplication table of a given number.

def mult_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

n=int(input("Enter a number: "))
mult_table(n)