class Employee:     #parent class
    company = "Google"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Fiverr"
#     def show(self):
#         print(f"The name of the programmer is {self.name} and the salary is {self.salary}")

class Programmer(Employee):  #child/inherited class
    company = "Fiverr"
    def showLanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")

e = Employee()
p= Programmer()

print(e.company, p.company)