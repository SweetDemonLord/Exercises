A={"Initial":1, "Middle":2, "Last":3}
B=dict(A)
C=A.copy()
D={k: v*10 for k, v in A.items()}
print("Sets are created:")
print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)
for k in A:
    A[k]*=100
print("After changing the original:")
print("A =",A)
print("B =",B)
print("C =",C)
print("D =",D)