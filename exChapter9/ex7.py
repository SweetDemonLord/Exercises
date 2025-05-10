class AddingFieldsClass:
    def __init__(self,lst1,lst2):
        self.lst1=lst1
        self.lst2=lst2
        if len(self.lst1)<len(self.lst2):
            self.lst1 += [0] * (len(self.lst2) - len(self.lst1))
        elif len(self.lst2)<len(self.lst1):
            self.lst2 += [0] * (len(self.lst1) - len(self.lst2))
    def __getitem__(self,index):
        return self.lst1[index]+self.lst2[index]
    def __setitem__(self,index,val1,val2):
        self.lst1[index] = val1
        self.lst2[index] = val2
    def __len__(self):
            return len(self.lst1)

A=AddingFieldsClass([100,200],[111,444,777])
for k in range(len(A)):
    print(A[k], end=" ")
