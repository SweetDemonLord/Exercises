try:
    print("Equation: Ax = B - A - 1")
    A, B=eval(input("Enter A and B (separated by commas): "))
    if A != 0:
        x = (B - 1) / A - 1
        print("Solution of the equation is", x)
    elif A == 0 and B == 1:
        print("Solution of the equation is any number.")
    elif A == 0 and B != 1:
        print("There are no solutions.")
except TypeError:
    print("TypeError: invalid operation")
except SyntaxError:
    print("SyntaxError: the expression cannot be converted to a number.")
except:
    print("Unexpected error.")