class FormationOfListField:
    def __init__(self, numerical_list):
        self.L=[]
        for i in numerical_list:
            if type(i)==int:
                self.L.append(i)
    def show(self):
        print("List field: ", self.L)
    def average(self):
        return sum(self.L)/len(self.L)
L=eval(input("Enter the list: "))
obj=FormationOfListField(L)
obj.show()
print("Average value of the list field: ", obj.average())