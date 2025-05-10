# Text representation for the command
txt="(2+3)/0.25-4*2.1"
# Showing expression and calculation of the result
print(txt,"=", eval(txt))
# Reading an expression for calculation
res=input("Enter an expression: ")
# Showing a value of the expression
print("The value of the expression:", eval(res))

x = "2**3"
print(x, "=", eval(x))