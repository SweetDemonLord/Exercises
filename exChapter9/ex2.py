class NewClass:
    def __init__(self, val):
        self.value = val
    def __str__(self):
        return "Text: "+str(self.value)
    def __int__(self):
        if self.value:
            return int(self.value)
        else:
            return 0
    def __float__(self):
        if self.value:
            return float(self.value)
        else:
            return 0
A=NewClass(14.11)
print(A)
print(int(A)-1)
print(float(A)-1)