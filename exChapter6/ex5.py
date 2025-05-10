def max_num(f,a,b):
    nl=[]
    for k in range(a,b+1):
        nl.append(f(k))
    return max(nl)
def equation(x):
    return x**2 - 4*x + 5
point1,point2=eval(input("Enter two numbers: "))
print("Maximum value of the first function is", max_num(lambda x: x*x,point1,point2))
print("Maximum value of the second function is", max_num(equation,point1,point2))