"""
np.delete(arr_name, index_number, axis=None)
"""

import numpy as np

#1d array
arr = np.array([10,20,30,40,50,7])
new_arrya = np.delete(arr, 5, axis=0)
print(new_arrya) #[10 20 30 40 50]

#2d array
arr2 = np.array([[1,2,3],[4,5,6]])
new_arr2d = np.delete(arr2, 0, axis=0)
print(new_arr2d) #[[4 5 6]]
new_arr2d = np.delete(arr2, 0, axis=1)
print(new_arr2d) 
"""
[[2 3]
 [5 6]]
 
 """
