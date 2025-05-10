class ArithmeticClass:
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return str(self.num)
    def __add__(self, other):
        return ArithmeticClass(self.num + other)
    def __sub__(self, other):
        return ArithmeticClass(self.num - other)
    def __rsub__(self, other):
        return ArithmeticClass(other - self.num)
    def __truediv__(self, other):
        return ArithmeticClass(self.num / other)
A=ArithmeticClass(50)
print("Object+operand:",A+27)
print("Object-operand:",A-27)
print("Operand-object:",77-A)
print("Object/operand:",A/5)