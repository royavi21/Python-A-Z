def func1():
    print("Hello from function 1")
func1()

def avg():  #define 'avg' function
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    avg=(a+b+c)/3
    print("Average of three numbers is: ", round(avg, 2))
avg()   #call the function
print("Thanks for using our program")
avg()   #again call the function.
#You can call functions anytime and anywhere in the program.
