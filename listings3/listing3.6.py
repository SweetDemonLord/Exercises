# Importing functions to generate random numbers
from random import *
# The function to display a nested list
def show(A):
    for a in A:
        for i in a:
            print(i, end=' ')
        print()
# The function to create a nested list
# from random number:
def rands(m, n):
    res=[[randint(0,9) for i in range(n)] for j in range(m)]
    return res
# The function to create a nested list of letters
def symbs(m, n):
    val='A'
    res=[['' for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j]=val
            val=chr(ord(val)+1)
    return res
# Create the nested list
A=[[(j+1)*10+i+1 for i in range(5)] for j in range(5)]
print("List A:")
# Display the nested list
show(A)
# Initializing the random numbers generator
seed(2019)
# A list of random numbers
B=rands(3,4)
print("List B:")
# Display the nested list
show(B)
# The list with letters
C=symbs(3,5)
print("List C:")
# Display the nested list
show(C)
# The list specifies a number of strings in the nested list
size=[3,5,4,6]
# Create the nested list
D=[['*' for k in range(s)] for s in size]
print("List D:")
# Display the nested list
show(D)