"""
np.split() 
equal

np.hsplit()
np.vsplit()
"""

import numpy as np

arr = np.array([10,20,30,40,50, 60])

print(np.split(arr, 3))

#[array([10, 20]), array([30, 40]), array([50, 60])]