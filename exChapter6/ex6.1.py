def apply_n_times(func,n):
    """Returns a function that applies a function n times."""
    def apply_n_times_inner(x):
        result=x
        for i in range(n):
            result=func(result)
        return result
    return apply_n_times_inner
def square(x):
    return x*x
N=int(input("Enter a number of times a function is applied: "))
power = apply_n_times(square,N)
value=int(input("Enter a number to square N times: "))
result=power(value)
print(result)
