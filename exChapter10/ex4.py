# A(A-1)x = sin(A)
from math import *
def solve(A):
    try:
        a=float(A)
    except:
        raise ValueError("Incorrect data format")
    if a==1:
        raise ArithmeticError("No solution")
    elif a==0:
        raise Warning("x = -1")
    return sin(a)/(a*(a-1))
print("* Solve the quadratic equation")
A=[1,0,2]
for k in range(len(A)):
    a=A[k]
    print("[",k+1, "] The equation: "+str(a)+"("+str(a)+" - 1) * x = ","sin("+str(a)+")",sep="")
    try:
        print("x =", solve(a))
    except ValueError as error:
        print("The equation must have only numbers")
        print(error)
    except ArithmeticError as error:
        print("Can't solve the equation")
        print(error)
    except Warning as error:
        print("A = 0")
        print(error)
print("* The program execution finished")