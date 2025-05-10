# A function with an inner function
def mysum(*a):
    # A list
    txt=["numbers","squares","cubes"]
    # An inner function
    def calc(n):
        s=0
        for m in range(len(a)):
            s+=a[m]**n
        return s
    # Calling the inner function
    for k in range(len(txt)):
        print("Sum", txt[k]+":", calc(k+1))
# Calling the function
mysum(1,3,5,7)