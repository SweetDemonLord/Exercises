class NewClass:
    def __init__(self, n,a):
        self.name = n
        self.age = a
    def show(self):
        print("Your name is "+self.name+".","Your age is", self.age)
name=input("What is your name? ")
age=input("How old are you? ")
A=NewClass(name,age)

NewClass.show(A)
A.show()