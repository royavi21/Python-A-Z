class Employee:     #parent class
    company = "Google"
    name = "Avijt"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all languages, the language is {self.language}")

class Programmer(Employee, Coder):  #multiple inheritance
    company = "Google"
    def showLanguage(self):
        print(f"The name is {self.company} and the language is {self.language}")

e = Employee()
p= Programmer()

p.show()
p.printLanguage()
p.showLanguage()
