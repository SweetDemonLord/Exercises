class Alpha:
    code=123
    def __init__(self,num):
        print("Constructor # 1")
        self.number=num
        print("An object has been created")
        self.show()
    def show(self):
        print("Method # 1")
        print("Class:",self.__class__.__name__)
        print("Code of the class:",self.code)
        print("Number field:",self.number)
class Bravo(Alpha):
    code=456
class Charlie(Bravo):
    def __init__(self,num,txt):
        print("Constructor # 2")
        self.number=num
        self.name=txt
        print("A new object has been created")
        self.show()
    def show(self):
        print("Method # 2")
        print("Class:",self.__class__.__name__)
        print("Code of the class:",self.code)
        print("Number field:",self.number)
        print("Name field:",self.name)
class Delta(Charlie):
    code=789
A=Alpha(100)
A.code=321
print("After the command A.code=321")
A.show()
B=Bravo(200)
C=Charlie(300,"C")
D=Delta(400,"D")