class Employee:
    a=1

    @classmethod 
    def show(cls):
        print(f"The class attribute of a is: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    # property and setter are the two decorators that work together
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e=Employee()
e.a=10  #Instance attribute created

e.name= "Avijit Roy"
print(e.fname, e.lname)

e.show()  #Prints the instance attribute value