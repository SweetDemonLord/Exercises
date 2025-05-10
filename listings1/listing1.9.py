# Reading a number of terms
n=input("Enter a number of terms: ")
# Variable with a text value
txt="1"
# Index variable
k=1
# Cycle operator for formatting text with
# an expression for the sum of natural numbers
while str(k)!=n:
    # Increase value of the index variable
    k=k+1
    # Adding a fragment to text with an expression
    # for the sum of natural numbers
    txt=txt+"+"+str(k)
# Showing the results
print(txt,"=", eval(txt))