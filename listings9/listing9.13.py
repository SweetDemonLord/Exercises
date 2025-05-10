class Alpha:
    # Method to get access to the attribute
    def __getattribute__(self,name):
        print("Alpha: field query", name)
        return object.__getattribute__(self,name)
    # The method is called if the attribute does not exist
    def __getattr__(self,name):
        print("The field is not existed!")
        return "Alpha: "+name
# Class with special method
class Bravo:
    # Method to get access to the attribute
    def __getattribute__(self,name):
        print("Bravo: field query", name)
        try:
            res=object.__getattribute__(self,name)
        except AttributeError:
            res="Bravo: no field "+name
        return res
# Creating objects and accessing fields
print("Object A of Alpha class")
A=Alpha()
A.value=123
print("Value field:",A.value)
print("One more time:", object.__getattribute__(A,"value"))
A.value=321
print("Value field:",A.value)
print(A.color)
print("Object B of Bravo class")
B=Bravo()
B.mylist=[1,2,3]
print("Mylist field:", B.mylist)
print("One more time:", object.__getattribute__(B,"mylist"))
B.mylist=["A","B","C"]
print("Mylist field:", B.mylist)
print(B.myset)