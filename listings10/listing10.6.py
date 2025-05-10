while True:
    res=input("Enter a natural number: ")
    try:
        # Attempting to convert to integer
        num=int(res)
        if num<1:
            msg="A number has to be a natural number"
            raise ArithmeticError(msg)
        # Exception handling
    except ArithmeticError as error:
        print(error)
    except:
        print("Input error")
    else:
        break
print("Amount from 1 to", num,"=",sum(range(num+1)))
