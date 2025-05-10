class MyClass:
    # Method for assignment a value to a field
    def set(self,n):
        self.number = n
    # Method for displaying a value of a field
    def show(self):
        print("Number field =",self.number)
A=MyClass()
B=MyClass()
A.set(100)
B.set(200)
# Checking field values
A.show()
B.show()
# Assignment field values to the objects
A.number=123
B.number=321
# Checking field values
A.show()
B.show()