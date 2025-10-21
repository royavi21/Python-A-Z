"""
reshape(wors, column) specify new shape
if dimentions match

1d -> 2d/3d convertion

"""

import numpy as np

arr = np.array([1,2,3,4,5,6])

reshape_arry = arr.reshape(2,3) #reshaping dosen't create copy; it's return view
print(reshape_arry)

"""
[[1 2 3]
 [4 5 6]]
 
"""