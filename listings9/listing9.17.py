class Alpha:
    # Method for reading value by index
    def __getitem__(self,index):
        return self.value[index]
    # Method for assigning value by index
    def __setitem__(self,index,val):
        self.value[index] = val
    # Method for deleting by index
    def __delitem__(self,index):
        del self.value[index]
    # Method for converting to the text format
    def __str__(self):
        return str(self.value)
    # Method for calculating "a length" of an object
    def __len__(self):
        return len(self.value)
A=Alpha()
# List field for the object
A.value=[100,200,300]
# Checking contains of the object
print(A)
# Operations with an object using an index
for k in range(len(A)):
    print(A[k], end=" ")
print()
A[1]="A"
print(A)
del A[0]
print(A)
