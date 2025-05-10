# Class with special method
class Alpha:
    def __getattr__(self,name):
        return len(name)
class Bravo:
    def show(self,x):
        print("Method show():",x)
    def __getattr__(self,name):
        if len(name)<5:
            return lambda x: print("The first method:",x)
        else:
            return lambda x: print("The second method:",x*x)
print("Object A of Alpha class")
A=Alpha()
A.value="Alpha"
print("Value field:",A.value)
print("Color field:",A.color)
print("Myattribute field:",A.myattribute)
print("Object B of Bravo class")
B=Bravo()
B.show(10)
B.hi(10)
B.display(10)