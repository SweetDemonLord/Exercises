# Description of a class
class MyClass:
    def __init__(self):
        self.value=123
        print("An object is created:",self.value)
    def __del__(self):
        print("An object is deleted:",self.value)
    # Method for assigning a value to a field
    def set(self,n):
        self.value=n
    # Method for displaying a value to a field
    def show(self):
        print("An object field:",self.value)
# Create an object
obj=MyClass()
# Calling a method from the object
obj.show()
obj.set(100)
# Calling a method from the class
MyClass.show(obj)
MyClass.set(obj,200)
obj.show()
# Explicit constructor call
MyClass.__init__(obj)
# Explicit destructor call
MyClass.__del__(obj)
# Checking a value of a field
obj.show()
# Changing the value of the field
obj.value=321
obj.show()
# Explicit constructor call
obj.__init__()
# Explicit destructor call
obj.__del__()
# Checking the field value via the object
obj.show()