# Creating sets
A={0,5,10,15,20}
B={10,15,20,25,30}
# Contents of sets
print("The sets are created:")
print("A=", A)
print("B=", B)
# Intersection of the sets
print("Intersection of A and B sets:")
A.intersection_update(B)
print("A=",A)
# Union of the sets
print("Union with {1,20,100}:")
A.update({1,20,100})
print("A =", A)
# Difference of the sets
print("Difference of B and A sets:")
B.difference_update(A)
print("B=",B)
# Symmetric difference of the sets
print("Symmetric difference of B and {30,35} sets:")
B.symmetric_difference_update({30,35})
print("B=",B)