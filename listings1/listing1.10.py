# Function for displaying from the text passed by the argument
def show(txt):
    # Convert text to a list and sort it
    symbs=sorted(list(txt))
    # Displaying contents of a list
    print(symbs)
# Calling a function
show("Python")
# Function for calculation sum of squares of natural numbers
def sqsum(n):
    # Creating a list of squares of natural numbers
    num=[k*k for k in range(1,n+1)]
    # Result of the function
    return num
# Variable with a numeric value
m=10
# Calling the function for calculation the sum of squares of natural numbers
print("The sum of squares of number from 1 to ", str(m)+":", sqsum(m))
