import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # shape(2, 3)

arr2 = np.array([10, 20]) # shape(2, )

result = arr1 + arr2
print(result) #ValueError: operands could not be broadcast together with shapes (2,3) (2,)

