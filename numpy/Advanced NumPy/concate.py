"""
np.concatenate((array, array2), axis = 0)

axis 0 -> vertical staking
axis 1 -> horizontal staking
"""

import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([4,5,6,7])

new_arr = np.concatenate((arr1,arr2))
print(new_arr)  #[1 2 3 4 4 5 6 7]

