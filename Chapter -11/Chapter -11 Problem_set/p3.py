# 3. Create a class ‘Employee’ and add salary and increment properties to it.Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

"""class Employee:
    salary = 180
    increment = 13
    
    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, salary):
        self.increment= ((salary/self.salary) -1)*100
    

e = Employee()
# print(e.SalaryAfterIncrement())
e.SalaryAfterIncrement = 280.8

print(e.increment)"""


class Employee:
    def __init__(self, salary=18000, increment=13):
        self.salary = salary
        self.increment = increment
    
    @property
    def SalaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, new_salary):
        # Set increment based on new salary
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()
print("Before:", e.increment, e.SalaryAfterIncrement)

e.SalaryAfterIncrement = 20000   # now logical: setting "new salary"
print("After:", e.increment, e.SalaryAfterIncrement)

