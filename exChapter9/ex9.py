class OddClass:
    def __init__(self, *n):
        lst=[]
        for i in n:
            if type(i)==int and i%2==1:
                lst.append(i)
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
A=OddClass(43,888,15,77,92,55,10,23)
try:
    while True:
        print(next(A), end=" ")
except StopIteration:
    print()