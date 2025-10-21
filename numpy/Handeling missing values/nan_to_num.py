#np.nan_to_num(array, nan=value) default - 0

import numpy as np
arr = np.array([1, 2, np.nan, 4, np.nan, 6])
clear_array = np.nan_to_num(arr)
print(clear_array) #[1. 2. 0. 4. 0. 6.]

cln_array = np.nan_to_num(arr, nan=44)
print(cln_array) #[ 1.  2. 44.  4. 44.  6.]