# A tuple of numbers
A=tuple(k for k in range(1,21) if k%3!=0)
print(A)
# A list of numbers
B=[2**(k//2) if k%2==0 else 3**(k//2) for k in range(15)]
print(B)
# A list of numbers
C=[0 if k==0 or k==1 else k**2 for k in range(13) if not k in [2,5,7]]
print(C)
# The tuple in reverse order
Alpha=A[::-1]
print(Alpha)
# Elements are selected "every other", starting from the first
Bravo=B[::2]
print(Bravo)
# Elements are selected "every other", starting from the second
Charlie=B[1::2]
print(Charlie)
