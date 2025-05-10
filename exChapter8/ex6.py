def list_of_objects(n,obj):
    l=[]
    for i in range(n):
        l.append(obj.__dict__[str(i)])
    print("The object field values are listed:",l)
class MyClass:
    def __init__(self,n):
        for k in range(n):
            self.__dict__[str(k)]=k*2+1
N=int(input("Enter the number of objects: "))
NewObject=MyClass(N)
list_of_objects(N,NewObject)