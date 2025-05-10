# Importing functions to generate random number
from random import *
# Function for displaying content of list,
# sets, text and dictionaries
def show(L, symb):
    for s in L:
        print(symb,s,sep="",end="")
    print(symb)
def show_dic(L, symb):
    for s in L.values():
        print(symb,s,sep="",end="")
    print(symb)
# Initial data
A=[1,2,3,4,5]           # The list
B={'A','B','C','D'}     # The set
C="Python"              # the text
D={"A":1,"B":2,"C":3}   # The dictionary
# Calling the function
show(A,"|")
show(B, "/")
show(C,"*")
show_dic(D,"#")
# Function for creating a list of numbers
def get_nums(n, state):
    if type(n)!=int:
        return []
    if state:
        L=list(2*(k+1) for k in range(n))
    else:
        L=list(2*k+1 for k in range(n))
    return L
# Calling the function
print(get_nums(10, True))
print(get_nums(8, False))
print(get_nums(12.5, True))
# Function for generating a set of random letters
def get_symbs(n):
    if n>10 or n<1:
        num=10
    else:
        num=n
    S=set()
    Nmin=ord("A")
    Nmax=ord("Z")
    while len(S)<num:
        S.add(chr(randint(Nmin,Nmax)))
    return S
# Initializing the generator of random number
seed(2019)
# Calling the function
print(get_symbs(7))
print(get_symbs(-5))
print(get_symbs(15))