from random import *
def randlist(r,c):
    res=[[randint(0,9) for i in range(r)] for j in range(c)]
    return res
def show(A):
    for a in A:
        for i in a:
            print(i,end=' ')
        print()
row, col=eval(input("Enter a number of rows and columns:"))
L=randlist(row,col)
show(L)
