myList = [1,2,9,5,3,5]

"""
squaredList = []
for item in myList:
    squaredList.append(item**2) #(item*item)
    """
    
#Using list comprehension
squaredList = [i*i for i in myList]
print(squaredList)