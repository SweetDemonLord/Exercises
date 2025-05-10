class MyClass:
    def __init__(self, n="White"):
        self.name = n
        print("An object is created:",self.name)
    def __del__(self):
        print("An object is deleted:",self.name)
def create(n):
    obj=MyClass(n)
A=MyClass()
B=MyClass("Red")
C=MyClass("Blue")
create("Yellow")
C.name="Green"
del A
del B
del C
