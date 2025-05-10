class ComparisonObject:
    def __init__(self, val):
        self.field_list=[]
        self.field_list.extend([k for k in val if isinstance(k, int)])
        self.field_list += [0] * (6 - len(self.field_list))
        #for k in val:
            #if type(k)==int:
                #self.field_list.append(k)
        #if len(self.field_list)<6:
            #for k in range(len(self.field_list)-1,6):
                #self.field_list.append(0)
    def __eq__(self, other):
        return self.field_list[0]==other.field_list[0]
    def __ne__(self, other):
        return self.field_list[1]!=other.field_list[1]
    def __lt__(self, other):
        return self.field_list[2]<other.field_list[2]
    def __gt__(self, other):
        return self.field_list[3]>other.field_list[3]
    def __le__(self, other):
        return self.field_list[4]<=other.field_list[4]
    def __ge__(self, other):
        return self.field_list[5]>=other.field_list[5]
A=ComparisonObject([77,5,3,4,25,6])
B=ComparisonObject([77,20,6,3,44,8])
print("A==B:",A==B)
print("A!=B:",A!=B)
print("A<B:",A<B)
print("A>B:",A>B)
print("A<=B:",A<=B)
print("A>=B:",A>=B)