def get_func(f,n):
    for i in range(1,n+1):
        f(i)
def func(x):
    print(x*x)
N=int(input("Enter a number of times a function is applied:"))
get_func(func,N)