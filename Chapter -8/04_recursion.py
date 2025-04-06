'''
                            Recursion
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 * 1
factorial(3) = 3 * 2 * 1
factorial(4) = 4 * 3 * 2 * 1
factorial(5) = 5 * 4 * 3 * 2 * 1

'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
n = int(input("Enter a number: "))
print(f"Factorial of {n} is:{factorial(n)}")