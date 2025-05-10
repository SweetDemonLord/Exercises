# Creating a tuple
A=(10,20,30)
print("A:", A)
B=("Python", (1,2))
print("B:", B)
# Calculating a sum of the tuple:
C=A+B
print("C:", C)
# Adding an elements to the end of the tuple
C+=(100,)
print("C:", C)
# Removing elements of the tuple:
C=C[:1]+C[2:]
print("C:", C)
# Adding an element at the beginning of the tuple
C=(200,)+C
print("C:", C)
# Replacement of element in the tuple
C=("A","B")+C[3:]
print("C:", C)
# Inserting elements into the tuple
C=C[:2]+(8,9)+C[2:]
print("C:", C)
# Assignment a value to an element of the tuple
C=C[:2]+(7,)+C[3:]
print("C:", C)