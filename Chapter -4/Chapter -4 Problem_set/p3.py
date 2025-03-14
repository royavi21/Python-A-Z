# 3. Check that a tuple type cannot be changed in python. 

a = (34, 345, "Avijit")

a[3] = "Roy"

print (a)


#This is the output, ,hens it's prove that tuple type can't be changed in python. 
'''

a[3] = "Roy"
    ~^^^
TypeError: 'tuple' object does not support item assignment

'''