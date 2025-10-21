#dtype() -> returns data type

import numpy as np

arr = np.array([1,2,3.5])
print(arr.dtype)  #float64

arr2 = np.array([1,2,5])
print(arr2.dtype)   #int64

arr3 = np.array(["Hello"])
print(arr3.dtype)   #<U5

arr4 = np.array(["Avijit"])
print(arr4.dtype)   #<U6