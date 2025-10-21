
#np.isnan(array)

import numpy as np

arr = np.array([1,2, np.nan, 4, np.nan, 6])

print(np.isnan(arr))

print(np.nan == np.nan)  # False