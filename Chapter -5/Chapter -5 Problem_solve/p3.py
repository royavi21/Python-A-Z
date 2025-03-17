#Can we have a set with 18 (int) and '18'(str) as a value in it?

s = set()

s.add(18)   #int
s.add("18") #str

print(s)
# Output: {'18', 18}


#Answer: Yes, we can. 