A=[10,20,30,40]
for k in [0,1,2,"three",4,3]:
    try:
        print("A["+str(k)+"] = ", end="")
        A[k]/=(k-1)
        print(A[k])
    except IndexError:
        print("there is no such items")
    except ZeroDivisionError:
        print(A[k], "- division by zero")
    except TypeError:
        print("wrong index type")