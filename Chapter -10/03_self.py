
class Employee:
    language = "Python" #This is a class attribute
    salary=20000

    def getInfo(self):
        print(f"The language is: {self.language}.\nThe salary is: {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

avi= Employee()
avi.language = "javaScript"

avi.greet()
# avi.getInfo()
#both does the same |
Employee.getInfo(avi)
