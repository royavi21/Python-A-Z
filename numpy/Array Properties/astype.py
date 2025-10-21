import numpy as np
#.astype() ->type convertion

arr = np.array([2.3,1.4,3.5])
print(arr.dtype)        #float64

int_arr = arr.astype(int)   # <--- type convertion using astype(type_name)

print(int_arr)          #[2 1 3]
print(int_arr.dtype)    #int64
