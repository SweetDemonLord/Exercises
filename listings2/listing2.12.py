# An expression is entered
val=eval(input("Enter an expression: "))
# The ternary operator is used
a, b=(val[0], val[-1]) if type(val)==str else (val, type(val))
# Variable values
print(a)
print(b)
