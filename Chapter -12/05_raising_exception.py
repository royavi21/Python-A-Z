
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if b==0:
    raise ZeroDivisionError("Hey, you cannot divide a number by zero")
else:
    print(a/b) 

# এখানে raise করার পর নিচের লাইনটি আর execute হবে না 
# আগে থেকেই exception raise হয়ে গেছে
print("I am done") #যদি b=0 হয় তাহলে এই লাইনটি execute হবে না। 