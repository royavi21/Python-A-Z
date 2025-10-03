# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them. 

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, c2):
        return Complex(self.real + c2.real, self.imag + c2.imag)

    def __mul__(self, c2):
        real_part = (self.real * c2.real) - (self.imag * c2.imag)
        imag_part = (self.real * c2.imag) + (self.imag * c2.real)
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print(c1 + c2)
print(c1 * c2)