
class Employee:
    language = "Python" #This is a class attribute
    salary=20000

    def __init__(self, name, salary, language): # dunder method which is automatically called.
        # শুধু __init__ মেথড একাই call হয়ে যাবে।
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an object.")

    def getInfo(self):
        print(f"The language is: {self.language}.\nThe salary is: {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

avi= Employee("Avijit Roy", 120000, "TypeScript")

# avi.name = "Avijit Roy"
print(avi.name, avi.salary, avi.language )

# avi.getInfo()

# rohaan = Employee()