# The original list
A=[1,3,[10,20],"Python",[40,50]]
# Creating a shallow copy of a list
B=A[:]
C=A.copy()
print("Original value:")
print("A:", A)
print("B:", B)
print("C:", C)
# Making changes to the original list
A[0]=[100,200]
A[2][1]=300
A[3]="Java"
A[4]=90

C[4][1]="C++"
print("After making changes:")
print("A:", A)
print("B:", B)
B[1]=77
print("C:", C)