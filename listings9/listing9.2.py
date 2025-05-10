class Alpha:
    code=123
    def alpha(self):
        print("Alpha:",self.code)
class Bravo(Alpha):
    def bravo(self):
        print("Bravo:",self.code)
class Charlie(Bravo):
    def charlie(self):
        print("Charlie:",self.code)
# Function to display inheritance hierarchy
def show(MyClass):
    print("Class",MyClass.__name__,end=":\n")
    for s in MyClass.__mro__:
        print("<",s.__name__,">",end="",sep="")
    print()
# Class inheritance hierarchy
show(Alpha)
show(Bravo)
show(Charlie)
# Create objects
A=Alpha()
B=Bravo()
C=Charlie()
# Calling methods
print("Object A")
A.alpha()
print("Object B")
B.alpha()
B.bravo()
print("Object C")
C.alpha()
C.bravo()
C.charlie()
# Assigning a value to a field
Bravo.code=321
print("Bravo.code=321 command is completed")
# Method invocation
print("Object C")
C.alpha()
C.bravo()
C.charlie()
print("Object A")
A.alpha()