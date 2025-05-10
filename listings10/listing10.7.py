def solve(A,B):
    try:
        a=float(A)
        b=float(B)
    except:
        raise ValueError("Incorrect data format")
    if a==0:
        if b!=0:
            raise ArithmeticError("There are no solutions")
        else:
            raise Warning("The solution is any number")
    return b/a
print("* Solve linear equations")
A=[2.5,2,"three",10,0,0.0]
B=[3.0,4,0,"five",5,0]
for k in range(len(A)):
    a=A[k]
    b=B[k]
    print("[",k+1,"] Equation: ",a,"*x = ",b,sep="")
    try:
        print("x =", solve(a,b))
    except ValueError as error:
        print("Unpleasant situation №1")
        print(error)
    except ArithmeticError as error:
        print("Unpleasant situation №2")
        print(error)
    except Warning as error:
        print("Strange situation")
        print(error)
print("* All equations are solved")