a=34    # Global variable

def fun():
    global a  # Referring to the global variable
    a=4 # Local variable
    
    print(a)
    
fun()
print(a)