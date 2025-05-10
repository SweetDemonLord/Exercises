def sum_int(*args):
    try:
        s=0
        for i in args:
            s+=int(i)
        return s
    except ValueError:
        print("Input has to be an integer")
        return 0
    except:
        print("Unknown error")
        return 0
print("Sum of the integer numbers is", sum_int(10,20,30,'A'))