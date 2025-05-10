class Fibonacci:
    def __init__(self, n):
        lst=[1,1]
        a=1
        b=1
        for i in range(n-2):
            a, b=b, a+b
            lst.append(b)
        self.nums=lst
        self.position=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.position+=1
        if self.position<len(self.nums):
            return self.nums[self.position]
        else:
            raise StopIteration
A=Fibonacci(7)
try:
    while True:
        print(next(A), end=" ")
except StopIteration:
    print()