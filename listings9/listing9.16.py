class Alpha:
    # The method is called if the attribute does not exist
    def __getattr__(self,name):
        return "there is no such attribute"
    # The method is called when the attribute is deleted
    def __delattr__(self,name):
        if name=="number":
            print("Cannot be deleted")
        else:
            object.__delattr__(self,name)
# Creating an object
A=Alpha()
# Operations with fields of the objects
A.value="object A"
print("value:",A.value)
del A.value
print("value:",A.value)
A.number=123
print("number:",A.number)
del A.number
print("number:",A.number)
del A.__dict__["number"]
print("number:",A.number)