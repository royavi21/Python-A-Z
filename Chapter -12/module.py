def myFunc():
    print("Hello")



if __name__ == "__main__":
    
    print("I'm inside main.py")  # This block will only run when module.py is executed directly, not when imported
    
    myFunc()
    print(__name__)  # This will print "__main__" when module.py is run directly