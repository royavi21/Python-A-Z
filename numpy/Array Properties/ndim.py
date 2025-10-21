#ndim
#n-> number | dim-> diamention
# Helps to find array's diamention

import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],[3,4,5]])
arr_3d = np.array([[[1,2],[3,4],[6,7],[4,9]]])

print(arr_1d.ndim)  #1  diamention array
print(arr_2d.ndim)  #2  diamention's array
print(arr_3d.ndim)  #3  diamention's array
