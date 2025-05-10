A={0,5,10,15,20}
B={10,15,20,25,30}
print("The sets are created:")
print("A =",A)
print("B =",B)
print("Intersection of A and B:")
A&=B
print("A =",A)
print("Union with set {1,20,100}:")
A|={1,20,100}
print("A =",A)
print("Difference of B and A:")
B-=A
print("B =", B)
print("Symmetric difference of B and {30,35}:")
B^={30,35}
print("B =",B)