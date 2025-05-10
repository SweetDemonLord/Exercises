def create_object(l,txt):
    class NewClass:
        def __init__(self):
            for k in range(len(l)):
                if type(l[k]) == str:
                   self.__dict__[l[k]]=k+1
        def show(self):
            print("Class name:",self.__class__.__name__)
            print("Object:",self.__dict__)
    NewClass.__name__=txt
    return NewClass()
text=input("Enter a name of a new class: ")
L=list(input("Enter a list: "))
obj=create_object(L,text)
obj.show()