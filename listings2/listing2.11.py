# A number is entered
num=int(input("Enter an integer number: "))
# Using the ternary operator
res="even" if num%2==0 else "odd"
# The message
print("This is a "+res+" number")