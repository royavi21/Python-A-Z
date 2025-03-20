# Write a program to find whether a given username contains less than 10 characters or not. 

a=input("Your username: ")

if (len(a)<10):
    print("Your given username is les than 10 characters")

elif(len(a)==10):
    print("Your username is exact 10 carectecter long")
else:
    print("All is well.")