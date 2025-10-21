"""
.ravel() -> views
.flatten() -> copy

"""

import numpy as np

arr_2d= np.array([[1,2,3,4,6],[3,6,8,9,3]])

print(arr_2d.ravel())       #view
print(arr_2d.flatten())     #copy