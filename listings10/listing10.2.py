A=[10,20,30,40]
for k in [0,1,2,"three",4,3]:
    try:
        print("* The value of element A[“+str(k)+”]: ", end="")
        A[k]/=(k-1)
        print(A[k])
    except (TypeError, IndexError) as error:
        print()
        print("Class exception:", error.__class__.__name__)
        print(error.__doc__)
        print("Basic class:", error.__class__.__bases__[0].__name__)
    except ZeroDivisionError as error:
        print()
        print("A division by zero error has occurred")
        print("Chain of inheritance:")
        for  s in error.__class__.__mro__:
            print(s.__name__)
        A[k]=0.0
        print(A[k],"is assigned to the element")