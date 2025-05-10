A={k for k in range(1,50) if k%3==0}
B={k for k in range(1,50) if k%4==0}
print((A|B)-(A&B))
print(A^B)
print((A-B)|(B-A))
print()
print(A)
print()
print(B)