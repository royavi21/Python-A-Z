#To add any element at the end of the array we use -append

import numpy as np

arr = np.array([2,3,4,5,6])
new_arr = np.append(arr, [40,30,20])
print(new_arr) #[ 2  3  4  5  6 40 30 20]