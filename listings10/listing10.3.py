A=[10,20,30,40]
for k in [0,1,2,"three",4,3]:
    # Outer scope
    try:
        print("* The value of element A["+str(k)+"]:")
        try:
            A[k]/=(k-1)
            print(A[k])
        except ZeroDivisionError:
            print("Attempting to divide by zero")
            A[k]=0.0
            print("A new value", A[k])
        else:
            print("No division by zero error")
        # The scope is executed if there is no error
        finally:
            print("# Completing the inner scope")
    except:
        print("Something went wrong")
print("The program has completed the execution")
