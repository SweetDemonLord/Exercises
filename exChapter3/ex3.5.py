from random import *
def show(A):
    for i in A:
        for j in i:
            print(j, end=' ')
        print()
row,column=eval(input("Enter a number of row and column you want to delete: "))
A=[[randint(0,9) for i in range(5)] for j in range(5)]
print("The original list:")
show(A)
for i in range(len(A)):
    A[i].pop(row)
A.pop(column)
print("The changed list:")
show(A)
