#np.isinf(array)  | 10^1000  | 1/0

import numpy as np
arr = np.array([1, 2, np.inf, 4, -np.inf, 6])
print(np.isinf(arr))  # [False False  True False  True False]