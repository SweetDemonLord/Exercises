# Creating a list
A=[10,20,30]
print("A:", A)
B=["Python", [1,2]]
print("B:", B)
# Calculating a sum of the lists:
C=A+B
print("C:", C)
# Adding an elements to the end of the list
C+=[100]
print("C:", C)
# Removing elements of the list:
C[1:2]=[]
print("C:", C)
# Adding an element at the beginning of the list
C=[200]+C
print("C:", C)
# Replacement of element in the list
C[:3]=["A","B"]
print("C:", C)
# Inserting elements into the list
C[2:2]=[8,9]
print("C:", C)
# Assignment a value to an element of the list
C[2:3]=[7]
print("C:", C)