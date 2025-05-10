class MyError(Exception):
    def __init__(self):
        self.values=[]
    # The method handles the addition operation
    def __add__(self,val):
        self.values.append(val)
        return self
def getMyError(n):
    try:
        if n<=1:
            raise MyError
        getMyError(n-1)
    except MyError as error:
        raise error+n
def getList(n):
    try:
        getMyError(n)
    except MyError as error:
        return error.values
A=getList(10)
print(A)
B=getList(7.5)
print(B)