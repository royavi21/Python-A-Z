"""
Stacking
-------
 vstack(): Stack arrays vertically (row-wise).
 hstack(): Stack arrays horizontally (column-wise).
"""

import numpy as np

arr1 = np.array([1,2,3,4])
                
arr2 = np.array([5,6,7,8])

print(np.vstack((arr1, arr2))) 

print(np.hstack(((arr1, arr2))))