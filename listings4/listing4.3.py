# Creating sets
A={2 * k + 1 for k in range(5)}
B={2 * k for k in range(5)}
C={2*k+1 for k in range(3,8)}
# Contents of sets
print("Sets are created:")
print("A=", A)
print("B=", B)
print("C=", C)
# Union of the sets
print("Union of the sets:")
print("A | B =", A.union(B))
print("B | A =", B.union(A))
print("A | C =", A|C)
# Intersection of the sets
print("Intersection of the sets:")
print("A & B =", A.intersection(B))
print("A & C =", A&C)
# Difference of the sets
print("Difference of the sets:")
print("A - C =", A-C)
print("C - A =", C-A)
# Symmetric difference of the sets
print("Symmetric difference of the sets:")
print("A ^ C =", A^C)
print("C ^ A =", C.symmetric_difference(A))
# The original sets
print("The original sets:")
print("A =", A)
print("B =", B)
print("C =", C)