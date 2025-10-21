import numpy as np

arr_2d = np.array([[2,3],[5,6]])
print(arr_2d)
"""
[[2 3]
 [5 6]]"""

#insert at index 1
new_2d_arr = np.insert(arr_2d, 1, [9,9], axis=0)
print(new_2d_arr)
"""
[[2 3]
 [9 9]
 [5 6]]"""

new_2d_n_array = np.insert(arr_2d, 2, [7,7], axis=1)
print(new_2d_n_array)
"""
[[2 3 7]
 [5 6 7]]"""
 
liu_2d = np.insert(arr_2d, 0, [1,1], axis=None) #None dile single line e cole asbe
print(liu_2d) #[1 1 2 3 5 6]