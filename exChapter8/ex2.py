class NewClass:
    def __init__(self, arg1, arg2):
        if type(arg1)==int and type(arg2)==int:
            self.sum=arg1+arg2
        elif type(arg1)==str and type(arg2)==str:
            self.txt=arg1+arg2
        elif type(arg1)==str and type(arg2)==int:
            self.number=arg2
            self.txt=arg1
        elif type(arg2)==str and type(arg1)==int:
            self.number=arg1
            self.txt=arg2
        else:
            print("Field must be integers or strings.")
    def show(self):
        L=["sum","txt","number"]
        for s in L:
            if s in dir(self):
                print(s,"=",self.__dict__[s])
text1="Insaf"
text2="Mudarisov"
num1=77
num2=44
A=NewClass(text1,text2)
B=NewClass(num1,num2)
C=NewClass(num1,text1)
D=NewClass(text1,num1)
A.show()
B.show()
C.show()
D.show()