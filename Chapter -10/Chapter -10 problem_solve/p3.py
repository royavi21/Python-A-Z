# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a=4

ox= Demo()
print(ox.a) # Printing class attribute because instance attribute is not created yet

ox.a = 0 # Creating instance attribute  
print(ox.a) # Printing instance attribute

print(Demo.a) # Printing class attribute to show that it is not changed