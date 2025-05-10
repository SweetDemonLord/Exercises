class Alpha:
    pass
class Bravo:
    name="Bravo"
    def display():
        print("Name field:", Bravo.name)
    def show(self):
        print("Value field:",self.value)
    def __init__(self):
        self.value=123
A=Alpha()
B=Bravo()
print("Alpha class")
n=1
for s in Alpha.__dict__:
    print("["+str(n)+"] "+s+":",Alpha.__dict__[s])
    n+=1
print("Bravo class")
n=1
for s in Bravo.__dict__:
    print("["+str(n)+"] "+s+":",Bravo.__dict__[s])
    n+=1
print("A object:",A.__dict__)
print("B object:",B.__dict__)
Bravo.display()
Alpha.display=Bravo.display
del Bravo.display
B.show()
A.color="Red"
B.show=lambda:print("B object:", B.value)
print("Alpha class")
n=1
for s in Alpha.__dict__:
    print("["+str(n)+"] "+s+":",Alpha.__dict__[s])
    n+=1
print("Bravo class")
n=1
for s in Bravo.__dict__:
    print("["+str(n)+"] "+s+":",Bravo.__dict__[s])
    n+=1
print("A object:",A.__dict__)
print("B object:",B.__dict__)
Alpha.display()
Bravo.show(B)
B.show()