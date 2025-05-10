# Class
class MyClass:
    def __init__(self, name, n=1):
        self.name=name
        if n==1:
            self.next=None
        else:
            self.next=MyClass(self.name, n-1)
    def __del__(self):
        print("Deleting:", self.code)
    # Method for filling a chain with codes
    def set(self,num=1):
        self.code=self.name+"["+str(num)+"]"
        print(self.code)
        if self.next!=None:
            self.next.set(num+1)
    # Method for displaying object codes in a chain
    def show(self):
        print(self.code)
        if self.next!=None:
            self.next.show()
# Creating a chain of objects
print("One object:")
A=MyClass("Alpha")
A.set()
#A.show()
print("Chain of objects:")
B=MyClass("Bravo",5)
B.set()
#B.show()
print("Starting from the third object:")
B.next.next.show()
# Deleting the objects
print("Deleting the objects:")
del A
del B