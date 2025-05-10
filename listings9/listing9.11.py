# Class with operator overloading
class Alpha:
    def __init__(self, lst):
        self.vals=[]
        if type(lst)==list:
            for n in lst:
                self.vals.append(n)
    # Method for converting to test format
    def __str__(self):
        return str(self.vals)
    # Unary operator "plus"
    def __pos__(self):
        x=self.vals[0]
        del self.vals[0]
        self.vals.append(x)
        return x
    # Unary operator "minus"
    def __neg__(self):
        x=self.vals[-1]
        del self.vals[-1]
        self.vals.insert(0,x)
        return self
    # Multiplication of an object by an operand
    def __mul__(self,v):
        self.vals.append(v)
        return self
    # Multiplication of an operand by an object
    def __rmul__(self,v):
        self.vals.insert(0,v)
        return self
    # Reduced form of the multiplication operation
    def __imul__(self,v):
        return self*v
# Creating an object
A=Alpha([1,"A",2])
# Performing operations with an object
print(A)
print(+A)
print(-A)
print(A*3)
print(4*A)
A*="Alpha"
print(A)