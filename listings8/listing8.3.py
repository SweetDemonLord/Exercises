class MyClass:
    def set(self,n):
        self.number = n
    def show(self):
        print("Number field =",self.number)
obj = MyClass()
print("Availability of the number field =",hasattr(obj,"number"))
try:
    obj.show()
except AttributeError:
    print("Number field is not set")
obj.number=123
print("Availability of the number field =",hasattr(obj,"number"))
obj.show()
obj.set(321)
obj.show()