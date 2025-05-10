class MyError(Exception):
    def __init__(self,code=0,msg="MyError exception"):
        self.code = code
        self.message = msg
    def __str__(self):
        txt=self.message+"\nError code: "+str(self.code)
        return txt
try:
    print("Create your own error")
    try:
        raise MyError(123)
    except MyError as error:
        print(error)
        error.code=321
        error.message="Same error MyError"
        raise
except Exception as error:
    print(error)