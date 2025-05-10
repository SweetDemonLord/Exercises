class Alpha:
    def alpha(self):
        print("Alpha class")
class Bravo:
    def bravo(self):
        print("Bravo class")
class Charlie:
    def charlie(self):
        print("Charlie class")
class Delta(Alpha,Bravo,Charlie):
    pass
# Inheritance hierarchy
print("Inheritance:")
k=1
for s in Delta.__mro__:
    print("["+str(k)+"]",s.__name__)
    k+=1
obj=Delta()
obj.alpha()
obj.bravo()
obj.charlie()