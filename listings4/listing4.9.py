n=50
E=set(range(1,n+1))
A={s for s in E if s%3==0}
B={s for s in E if s%11==0}
C={s for s in E if s%7==0}
D={s for s in E if s%5==0}
N=(A|B)-(C|D)
print(N)