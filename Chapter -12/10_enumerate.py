l = [4,34,234, 23]

"""
index = 0
for item in l:
    print(f"At index {index} the value is {item}")
    index += 1
    


"""
#this can be done using enumerate function

for index, item in enumerate(l):
    print(f"At index {index} the value is {item}")