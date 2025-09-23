CHAPTER 11 - INHERITANCE & MORE ON OOPS 
Inheritance is a way of creating a new class from an existing class. 
Syntax: 
class Employee:  # Base class  
# Code 
class Programmer(Employee): # Derived or child class 
# Code 
We can use the method and attributes of ‘Employee’ in ‘Programmer’ object. 
Also, we can overwrite or add new attributes and methods in ‘Programmer’ class. 
TYPES OF INHERITANCE 
• Single inheritance 
• Multiple inheritance 
• Multilevel inheritance 
SINGLE INHERITANCE 
Single inheritance occurs when child class inherits only a single parent class. 
42 
MULTIPLE INHERITANCE 
Multiple Inheritance occurs when the child class inherits from more than one parent 
classes.
 MULTILEVEL INHERITANCE 
When a child class becomes a parent for another child class. 
SUPER() METHOD  
super() method is used to access the methods of a super class in the derived class. 
super().__init__() 
# __init__() Calls constructor of the base class 
43 
CLASS METHOD 
A class method is a method which is bound to the class and not the object of the class. 
@classmethod decorator is used to create a class method. 
Syntax: 
@classmethod 
def(cls,p1,p2): 
@PROPERTY DECORATORS 
Consider the following class: 
class Employee: 
@property 
def name(self): 
return self.ename 
If e = Employee() is an object of class employee, we can print (e.name) to print the 
ename by internally calling name() function. 
@.GETTERS AND @.SETTERS 
The method name with ‘@property’ decorator is called getter method. 
We can define a function + @ name.setter decorator like below: 
@name.setter 
def name (self,value): 
self.ename = value 
OPERATOR OVERLOADING IN PYTHON  
Operators in Python can be overloaded using dunder methods. 
These methods are called when a given operator is used on the objects. 
Operators in Python can be overloaded using the following methods: 
p1+p2 # p1.__add__(p2) 
p1-p2 # p1.__sub__(p2) 
p1*p2 # p1.__mul__(p2) 
p1/p2 # p1.__truediv__(p2) 
p1//p2 # p1.__floordiv__(p2) 
Other dunder/magic methods in Python: 
str__() # used to set what gets displayed upon calling str(obj) 
44 
__len__() # used to set what gets displayed upon calling.__len__() or 
len(obj) 