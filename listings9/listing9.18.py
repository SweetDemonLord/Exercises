class Fibs:
    def __getitem__(self,n):
        a=1
        b=1
        for k in range(n-2):
            a,b=b,a+b
        return b
F=Fibs()
for k in range(1,16):
    print(F[k], end=" ")
print()