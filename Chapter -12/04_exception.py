try:
    a=int(input("Hey, enter a number: "))
    print(f"You entered: {a}") 
    
# except ValueError as v:
#     print(v) 
    
except Exception as e:
    print(e)