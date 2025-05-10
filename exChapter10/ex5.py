class MyError(Exception):
    def __init__(self):
        self.values=[]
    # The method handles the addition operation
    def __add__(self,val):
        self.values.append(val)
        return self
def getMyError(ch):
    try:
        if ord(ch)>=ord('Z'):
            raise MyError
        getMyError(chr(ord(ch)+1))
    except MyError as error:
        raise error+ch
def getList(n):
    try:
        getMyError(n)
    except MyError as error:
        return error.values
A=getList('A')
print(A)