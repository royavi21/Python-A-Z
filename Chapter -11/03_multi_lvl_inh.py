class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manaer(Programmer):
    c=3

o=Employee()

print(o.a)  #Prints the a attribute of Employee class
# print(o.b)  #Shows error as b is not present in Employee class
# print(o.c)  #Shows error as c is not present in Employee class

o=Programmer()
print(o.a, o.b)

o=Manaer()
print(o.a, o.b, o.c)