print("Operations with a list of numbers...")
# Controlled code
try:
    nums=eval(input("Enter the list of numbers: "))
    print("Received the value: "+str(nums))
    a=int(nums[0])
    b=int(nums[3])
    print(str(a)+"/"+str(b)+"="+str(a/b))
# Exceptions handling
except ValueError:
    print("ValueError: conversion error!")
except ZeroDivisionError:
    print("ZeroDivisionError: attempting to divide by zero!")
except TypeError:
    print("TypeError: invalid input!")
except IndexError:
    print("IndexError: attempting to index out of range!")
except SyntaxError:
    print("SyntaxError: the expression cannot be calculated!")
except NameError:
    print("NameError: invalid identifier!")
print("Completion of the program.")