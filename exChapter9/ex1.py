class Alpha:
    name="Insaf"
    def show(self):
        print("Your name: ", self.name)
class Bravo(Alpha):
    date_of_birth = "14.11.2001"
    def show(self):
        print("Your name: ", self.name)
        print("Your date of birth: ", self.date_of_birth)
class Charlie(Bravo):
    residence="Sterlitamak"
    def show(self):
        print("Your name: ", self.name)
        print("Your date of birth: ", self.date_of_birth)
        print("Your place of residence: ", self.residence)
A=Alpha()
A.show()
B=Bravo()
B.show()
C=Charlie()
C.show()
