# Reading an upper limit of the sum
n=int(input("Enter a number: "))
# Initial value of the sum
s=0
# Initial value of the index variable
k=0
# Operator of the cycle for calculating the sum
while k<n:
    # Increase the value of the index variable by one:
    k=k+1
    # Adding a term to a sum
    s=s+k
# Showing the result:
print("Sum of numbers from 1 to ", n, "equals", s)
u=0
u=sum(list(range(1,n+1)))
print("Sum of numbers from 1 to ", n, "equals", u)
