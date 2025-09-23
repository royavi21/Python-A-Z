class Employee:
    def __init__(self):
        print("Constructor of Employee class called")
    a=1

class Programmer(Employee):
    def __init__(self):
        super().__init__()  #calls the constructor of parent class via super()
        print("Constructor of Programmer class called")
    b=2

class Manager(Programmer):
    def __init__(self):
        super().__init__() #calls the constructor of parent class via super()
        print("Constructor of Manager class called")
    c=3

o=Manager()

print(o.a, o.b, o.c)  #Prints the a attribute of Employee class


# o=Programmer()
# print(o.a, o.b)

# o=Manager()
# print(o.a, o.b, o.c)