class MyClass:
    def __init__(self, val):
        self.value = val
    # Method for conversion to text type
    def __str__(self):
        return "Field "+str(self.value)
    # Method for conversion to boolean type
    def __bool__(self):
        if type(self.value) == int:
            return True
        else:
            return False
    # Method for conversion to integer type
    def __int__(self):
        if self:
            return self.value
        else:
            return 0
# Creating objects and checking methods
print("Object A:")
A=MyClass(100)
print(A)
print("Number",int(A))
print("A - 1 =", int(A)-1)
print("Object B:")
B=MyClass("B")
print(B)
print("Number",int(B))
print("B + 1 =", int(B) + 1)
