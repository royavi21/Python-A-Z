

a = int (input("Enter your age: "))

#if statement no.1
if(a%2 == 0):
    print(f"{a} is even number")

else:
    print(f"{a} is odd number")
#end of no.1 if statement


#if statement no.2
if(a>=18):
    print("You are above 18")

elif(a==0):
    print("You entered 0 that is not a valid age!")

else:
    print("You are below 18 years old")

#end of no.2 if statement



'''IMPORTANT NOTES: 
1. There can be any number of elif statements. 
2. Last else is executed only if all the conditions inside elifs fail.'''