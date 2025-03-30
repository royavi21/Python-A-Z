 # Write a program to print multiplication table of n using for loops in reversed order.


n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

'''
Output:
Enter a number: 7
7 X 10 = 70
7 X 9 = 63
7 X 8 = 56
7 X 7 = 49
7 X 6 = 42
7 X 5 = 35
7 X 4 = 28
7 X 3 = 21
7 X 2 = 14
7 X 1 = 7
'''