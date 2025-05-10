class MyClass:
    def __init__(self, num):
        self.code=num
    # Method for converting to test format
    def __str__(self):
        return str(self.code)
    # Method for overloading the addition operator
    def __add__(self, n):
        if type(n)==int:
            val=self.code+n
        else:
            val=0
        return MyClass(val)
# Creating an object and checking methods
A=MyClass(100)
print("Object A:",A)
# A number is added to the object
B=A+25
print("Object B:",B)
# Text is added to the object
C=A+"Hello"
print("Object C:",C)