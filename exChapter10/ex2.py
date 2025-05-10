while True:
    try:
        lower, upper = eval(input("Enter lower and upper limits (integers): "))
        num1=int(lower)
        num2=int(upper)
        if num1<1 or num2<1:
            msg="The numbers have to be natural numbers"
            raise ArithmeticError(msg)
        elif num1>num2:
            msg="The lower limit is greater than the upper limit"
            raise ValueError(msg)
    except ArithmeticError as error:
        print(error)
    except ValueError as error:
        print(error)
    except:
        print("Input error")
    else:
        break
print("All integers in range",lower,"-",upper,":")
for lower in range(lower,upper+1):
    print(lower, end=" ")