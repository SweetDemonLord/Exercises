a,b=eval(input("Enter two floating-point numbers: "))
try:
    print("The first number is greater") if a>b else print("The second number is greater")
except TypeError:
    print("TypeError: invalid operation")
except SyntaxError:
    print("SyntaxError: the expression cannot be calculated")
except:
    print("Something went wrong")
print("The program is over")