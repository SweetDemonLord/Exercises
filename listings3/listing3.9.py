# Importing functions to create a deep copy
import copy
# The original list
A=[1,3,[10,20],"Python",[40,50]]
# Creating a deep copy of the list
B=copy.deepcopy(A)
print("Original values:")
print("A:", A)
print("B:", B)
# Making changes in the original list
A[0]=[100,200]
A[2][1]=300
A[3]="Java"
A[4]=90
print("After making changes:")
print("A:", A)
print("B:", B)