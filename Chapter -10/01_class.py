class Employee:
    language = "Python" #This is a class attribute
    salary=20000


avi= Employee()
avi.name = "Avijit Roy" #This is an instance/object attribute
print(avi.name, avi.language, avi.salary)

rohan = Employee()
rohan.name = "Rohan Haru"   #This is an instance/object attribute
print(rohan.language, rohan.salary, rohan.name)

#Here name is object attribute and salary & language are class attribute as they directly belong to the class