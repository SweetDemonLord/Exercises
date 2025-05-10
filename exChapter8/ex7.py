class MyClass:
    def __init__(self, l):
        self.l = l
    def show(self):
        print("List of summarized objects:",self.l)
def sum_of_objects(obj1,obj2):
    l=[]
    if len(obj1.l)>len(obj2.l):
        for i in range(len(obj2.l),len(obj1.l)):
            obj2.l.append(0)
    elif len(obj1.l)<len(obj2.l):
        for i in range(len(obj1.l),len(obj2.l)):
            obj1.l.append(0)
    for i in range(len(obj1.l)):
        l.append(obj1.l[i]+obj2.l[i])
    obj=MyClass(l)
    return obj
L1=eval(input("Enter the first list: "))
L2=eval(input("Enter the first list: "))
object1=MyClass(L1)
object2=MyClass(L2)
sum_of_objects(object1,object2).show()