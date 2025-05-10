# (A^2-1)x = B
def solve(A,B):
    try:
        a=float(A)
        b=float(B)
    except:
        raise ValueError("Incorrect data format")
    if a==1 or a==-1:
        if b!=0:
            raise ArithmeticError("No solution")
        else:
            raise Warning("Solution is any number")
    return b/(a**2-1)
print("* Solve the quadratic equation")
A=[2.5,2,"one",10,1,-1.0,5]
B=[3.0,4,"five",5,0,7,24]
for k in range(len(A)):
    a=A[k]
    b=B[k]
    print("[",k+1, "] The equation: ("+str(a)+"^2 - 1) * x = ",b,sep="")
    try:
        print("x =", solve(a,b))
    except ValueError as error:
        print("The equation must have only numbers")
        print(error)
    except ArithmeticError as error:
        print("№1 Can't solve the equation")
        print(error)
    except Warning as error:
        print("№2 Can't solve the equation")
        print(error)
print("* The program execution finished")