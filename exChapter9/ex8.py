class PolynomialSum:
    def __init__(self, lst):
        self.lst = lst
    def __call__(self, x):
        sum=0
        for i in range(len(self.lst)):
            sum += self.lst[i]*x**i
        return sum
A=PolynomialSum([10,20,30])
print("A(5) = ", A(5))