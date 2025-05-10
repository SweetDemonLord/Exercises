class Alpha:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("Your name: ", self.name)
class Bravo(Alpha):
    def __init__(self, name, date_of_birth):
        super().__init__(name)
        self.date_of_birth = date_of_birth
    def show(self):
        super().show()
        print("Your date of birth: ", self.date_of_birth)
class Charlie(Bravo):
    def __init__(self, name, date_of_birth, residence):
        super().__init__(name, date_of_birth)
        self.residence=residence
    def show(self):
        super().show()
        print("Your place of residence: ", self.residence)
name=input("Enter your name: ")
A=Alpha(name)
A.show()
date_of_birth=input("Enter your date of birth: ")
B=Bravo(name,date_of_birth)
B.show()
residence=input("Enter your place of residence: ")
C=Charlie(name,date_of_birth,residence)
C.show()