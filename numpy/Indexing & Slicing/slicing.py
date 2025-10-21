# start | stop |step
"""
slicing

array[start:step:step]
array[start:end], start to end -1

negative step, -1 revers

"""
import numpy as np

arr = np.array([2,3,4,56,7,8])
print(arr[1:4])     #[ 3  4 56] index 1 to 3
print(arr[:4])      #[ 2  3  4 56]  index 0 to 3
print(arr[::2])     #[2 4 7]  every 2nd element
print(arr[::-1])    #[ 8  7 56  4  3  2]    revers the arr (step 1)