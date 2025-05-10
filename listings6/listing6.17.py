def show(txt):
    """This is show() function with one argument."""
    print("The only argument",txt)
def display(a,b):
    """This is display() function with two arguments."""
    print("[1] The first argument",a)
    print("[2] The second argument",b)
# Function without documentation
def hello():
    print("Hello everyone!")
# Calling functions and checking documentation
print(show.__doc__)
show("A")
print(display.__doc__)
display("B","C")
# The variable refers to a function
fac=show
# Calling functions and checking documentation
print(fac.__doc__)
fac("D")
# New documentation text for functions
display.__doc__="New text for display()"
# Checking the result
print(display.__doc__)
display("E","F")
# Documentation for the function is being created
hello.__doc__="hello() function"
# Checking the result
print(hello.__doc__)
hello()