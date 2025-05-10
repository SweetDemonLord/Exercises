num=int(input("Enter a number: "))
one=1
N=0
for bit in range(num):
    N=N+1 if one<<bit & num else N
print("The sum of the values of all bits in binary representation of {} is {}".format(num,N))