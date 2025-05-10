def geometric_progression(k,n):
    if n==1:
        return 1
    elif n==2:
        return k
    else:
        return geometric_progression(k,n-1)*k
K=int(input("Enter the value of K:"))
N=int(input("Enter the value of N:"))
sum_gp=0
for i in range(1,N+1):
    sum_gp+=geometric_progression(K,i)
print("The sum of geometric progression is",sum_gp)