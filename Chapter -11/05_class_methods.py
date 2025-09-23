class Employee:
    a=1

    @classmethod # @classmethod ছাড়া run করলে value 10 প্রিন্ট হবে। এটা সহ করলে class attribute value প্রিন্ট হবে মানে 1

    def show(cls):
        print(f"The class attribute of a is: {cls.a}")

e=Employee()
e.a=10  #Instance attribute created

e.show()  #Prints the instance attribute value