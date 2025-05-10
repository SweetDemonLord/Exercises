class Alpha:
    def __init__(self, *vals):
        L=[]
        for v in vals:
            if type(v)==int:
                L.append(v)
        self.nums=L
    # The method is called when calling the iter() function
    def __iter__(self):
        return Bravo(self.nums)
class Bravo:
    def __init__(self, nums):
        L=[]
        for n in nums:
            if n<10 and n>0:
                L.append(n)
        self.digits=L
        self.position=-1
    # The method is called when calling the next() function
    def __next__(self):
        self.position+=1
        if self.position<len(self.digits):
            return self.digits[self.position]
        else:
            raise StopIteration
# Creating an object of Alpha class
A=Alpha(2,"A",12,7,-3,"Hello",9,5,"Alpha")
# Creating an object of Bravo class
B=iter(A)
# Calling next() function
try:
    while True:
        print(next(B), end=" ")
except StopIteration:
    print()