class Alpha:
    def __init__(self, num):
        self.code=num
        print("Assigned value to a code field")
    def show(self):
        print("Code field:",self.code)
class Bravo(Alpha):
    def __init__(self, num, txt):
        super().__init__(num)
        self.name=txt
    print("Assigned value to a name field")
    def show(self):
        # Calling a method from a base class
        super().show()
        print("Name field:",self.name)
class Charlie(Bravo):
    def __init__(self, num, txt, val):
        super().__init__(num, txt)
        self.value=val
        print("Assigned value to a value field")
    def show(self):
        super().show()
        print("Value field:",self.value)
# Creating objects and calling methods
print("Object A")
A=Alpha(100)
A.show()
print("Object B")
B=Bravo(200,"B")
B.show()
print("Object C")
C=Charlie(300,"C",[1,2,3])
C.show()