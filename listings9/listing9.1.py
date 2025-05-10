# Based class
class Alpha:
    def __init__(self):
        self.set(100)
        print("Object of class Alpha:",self.number)
    def set(self,n):
        self.number = n
    def show(self):
        print(self.__class__.__name__,self.number)
# Derived class
class Bravo(Alpha):
    def __init__(self):
        self.set(200)
        print("Object of class Bravo:",self.number)
# Base class object
A=Alpha()
A.set(123)
A.show()
# Derived class object
B=Bravo()
B.set(321)
B.show()