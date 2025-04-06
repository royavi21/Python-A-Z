# Write a recursive function to calculate the sum of first n natural numbers.

def sum_of_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_n(n-1)
n = int(input("Enter a number: "))
print(f"Sum of first {n} natural numbers is:{sum_of_n(n)}")