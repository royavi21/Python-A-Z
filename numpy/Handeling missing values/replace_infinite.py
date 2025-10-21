import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

print(np.isinf(arr))

cln_array = np.nan_to_num(arr, posinf=999, neginf=-999)
print(cln_array)  # [   1.    2.  999.    4. -999.    6.]