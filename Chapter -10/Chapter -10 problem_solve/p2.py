# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number

class Calculator:
    def __init__(self, n):
        self.n = float(n)  # store as number

    def square(self):
        print(f"The square is {self.n ** 2:.2f}")

    def cube(self):
        print(f"The cube is {self.n ** 3:.2f}")

    def squareroot(self):
        print(f"The square root is {self.n ** 0.5:.2f}")  # or math.sqrt(self.n)


a = Calculator(input("Enter your number for square, cube and root: "))
a.square()
a.cube()
a.squareroot()
