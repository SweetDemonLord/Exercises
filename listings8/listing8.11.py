# The function receives a reference to a class as an argument and
# returns a reference to the class as a result
def F(Alpha):
    # An inner class:
    class Bravo:
        value=Alpha()
    Bravo.__name__="My"+Alpha.__name__
    return Bravo
# Class Description
class Charlie:
    # Constructor
    def __init__(self):
        self.number=123
    # Method for displaying a field value
    def show(self):
        print("Number field:",self.number)
# Creating an object based on the class,
# obtained from a function call
obj=F(Charlie)()
# Checking a result
obj.value.show()
print("Object class obj:", obj.__class__.__name__)
print("Field class value:", obj.value.__class__.__name__)