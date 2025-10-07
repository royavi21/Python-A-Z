def main():
    try:
        a=int(input("Enter a number: "))
        print(a)
        return
        
    except Exception as e:
        print(e)
        return

    finally:
        print("I'm inside of finally block")

main()
    
    # finally block will always execute whether exception is there or not. 
    
"""try:
    a=int(input("Enter a number: "))
        print(a)
        
except Exception as e:
        print(e)
        
finally:
    print("I'm inside of finally block")""" 