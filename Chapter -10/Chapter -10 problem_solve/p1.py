# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company= "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a= Programmer("Avijit", 12000, 8120)
print(a.name, a.salary, a.pin, a.company)

r= Programmer("Rohan", 52000, 8121)
print(r.name, r.salary, r.pin, a.company)

"""
OP:
Avijit 12000 8120 Microsoft
Rohan 52000 8121 Microsoft

"""
