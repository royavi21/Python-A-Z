class Number:
    def __init__(self, n):
        self.n = n
        
    def __add__(self, num):  #Operator overloading
        return self.n + num.n

n=Number(1)
m=Number(2)
print(n + m)  #Error: unsupported operand type(s) for +: 'Number' and 'Number' Those are strings, we can't add them directly

#কিন্তু add method টা define করলে আমরা + operator দিয়ে add করতে পারব। এটা operator overloading হয়।


"""
1+p2 # p1.__add__(p2) 
p1-p2 # p1.__sub__(p2) 
p1*p2 # p1.__mul__(p2) 
p1/p2 # p1.__truediv__(p2) 
p1//p2 # p1.__floordiv__(p2) 

str__() # used to set what gets displayed upon calling str(obj) 

__len__() # used to set what gets displayed upon calling.__len__() or 
len(obj) 

"""
#Time stamp: 7:48:07