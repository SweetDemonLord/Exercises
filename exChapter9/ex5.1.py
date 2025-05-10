class CompareObject:
    def __init__(self, values):
        self.values = values
    def __eq__(self, other):
        return self.values[0] == other.values[0] if len(self.values) > 0 and len(other.values) else False
    def __ne__(self, other):
        return self.values[1] != other.values[1] if len(self.values) > 1 and len(other.values) > 1 else False
    def __lt__(self, other):
        self_value=self.values[2] if len(self.values) > 2 else 0
        other_value=other.values[2] if len(other.values) > 2 else 0
        return self_value < other_value
    def __gt__(self, other):
        self_value=self.values[3] if len(self.values) > 3 else 0
        other_value=other.values[3] if len(other.values) > 3 else 0
        return self_value > other_value
    def __le__(self, other):
        self_value = self.values[4] if len(self.values) > 4 else 0
        other_value = other.values[4] if len(other.values) > 4 else 0
        return self_value <= other_value
    def __ge__(self, other):
        self_value = self.values[5] if len(self.values) > 5 else 0
        other_value = other.values[5] if len(other.values) > 5 else 0
        return self_value >= other_value
obj1=CompareObject([77,5,3,4,25,6])
obj2=CompareObject([77,20,6,3,44,8])
print("A==B:",obj1==obj2)
print("A!=B:",obj1!=obj2)
print("A<B:",obj1<obj2)
print("A>B:",obj1>obj2)
print("A<=B:",obj1<=obj2)
print("A>=B:",obj1>=obj2)