class NewClass:
    def __init__(self,l):
        self.list=l
    def show(self):
        print("After adding objects:", end=" ")
        for k in self.list:
            print(k, end=" ")
def adding_objects(obj1,obj2):
    lst = []
    for k in range(len(obj1.list)):
        lst.append(obj1.list[k] + obj2.list[k])
    obj=NewClass(lst)
    return obj
A=NewClass([88,26,97])
B=NewClass([11,77,35])
C=adding_objects(A,B)
C.show()
