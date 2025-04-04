#Function ith arguments

'''
Here we are using the function with arguments.
greet_user() function takes two arguments name and ending.

'''

def greet_user(name, ending):
    print("Good day!", name)
    print(ending)

# Calling the function
greet_user("Avijit", "Thank you")    #ei avijit ke store kora hocche uporer namme paramiter e.
greet_user("Rohan", "Thank you")
greet_user("Sikha", "Thanks")


def greet (name):
    gr = "hello" + name
    return gr
a = greet("Avijit")
print(a)