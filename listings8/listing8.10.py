class Alpha:
    "This is Alpha class"
    pass
class Bravo:
    "This is Bravo class"
    pass
print(Alpha.__doc__)
print(Bravo.__doc__)
A=Alpha()
B=Bravo()
Alpha.__doc__="The first class"
B.__class__.__doc__="The second class"
print(A.__class__.__doc__)
print(B.__doc__)