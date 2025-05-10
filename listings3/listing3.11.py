# Connecting functions for generating random number
from random import *
# Initialization the random numbers generator
seed(2024)
# Creating a list of random numbers
A=[randint(10,20) for k in range(15)]
# Contents of the list
print("A:", A)
# Counting items with different values
for a in range(min(A), max(A)+1):
    print(a,"-", A.count(a))
# The greatest, the smallest and the average values
print("The smallest:")
print("A[", A.index(min(A)), "]=", min(A), sep="")
print("The greatest:")
print("A[", A.index(max(A)), "]=", max(A), sep="")
print("The average:", sum(A)/len(A))
# Sorting the list
B=sorted(A)
A.sort(reverse=True)
# Checking contents of the lists
print("A:", A)
print("B:", B)