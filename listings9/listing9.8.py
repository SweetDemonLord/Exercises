class Alpha:
    def __init__(self, num):
        self.code = num
    def show(self):
        print("Alpha class:", self.code)
class Bravo(Alpha):
    def show(self):
        print("Bravo class:", self.code)
        super().show()
class Charlie(Alpha):
    def show(self):
        print("Charlie class:", self.code)
        super(Charlie,self).show()
class Delta(Bravo,Charlie):
    # Method override
    def show(self):
        print("Delta class:", self.code)
        super().show()
        Charlie.show(self)
        super(Bravo,self).show()
# Function for displaying the inheritance chain
def display(MyClass):
    print("Inheritance for "+MyClass.__name__+":")
    k=1
    for s in MyClass.__mro__:
        print("["+str(k)+"] "+s.__name__)
        k+=1
# Displaying inheritance chains
# creating objects and calling methods
display(Alpha)
A=Alpha(100)
A.show()
display(Bravo)
B=Bravo(200)
B.show()
display(Charlie)
C=Charlie(300)
C.show()
display(Delta)
D=Delta(400)
D.show()