# CONDITIONAL EXPRESSION
# # if elif else are conditional methoods | function

'''
Sometimes we want to play PUBG on our phone if the day is Sunday. 
Sometimes we order Ice Cream online if the day is sunny. 
Sometimes we go hiking if our parents allow. 
All these are decisions which depend on a condition being met. 
IF ELSE AND ELIF IN PYTHON 
In python programming too, we must be able to execute instructions on a condition(s) 
being met. 
This is what conditionals are for! 
'''

a = int (input("Enter your age: "))

if(a>=18):
    print("You are over 18 years old") # লাইনের প্রথমে যে ৪ টা স্পেস আসছে তাকে indent বলে। Whitespace
    print("Good for you")

elif(a<0):
    print("You entered an invalid age nigga!")

elif(a==0):
    print("You entered 0 that is not a valid age!")

else:
    print("You are below 18 years old")
