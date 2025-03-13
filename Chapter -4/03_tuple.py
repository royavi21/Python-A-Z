a = (1,2,3,4)
print(type(a))

b=() # this is a empty tuple
print(type(b))

c = (1) # this is not a single value tuple, this is a int
print(type(c))

d = (777,) # this is a single value tuple
print(type(d))

e = (1,2.32, "Hanumankind", True, "Rolex")
#e[0] = 2   #tuple is immutable, so the 0 index value is not changing. Tuple is as like string - immutable
print(e)