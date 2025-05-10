from threading import *
from time import sleep
def factorial():
    global fac, num1
    for i in range(2,num1+1):
        fac*=i
        sleep(0.2)
def double_factorial():
    global dfac, num2
    if num2 % 2 == 0:
        for i in range(num2,1,-2):
            dfac*=i
            sleep(0.2)
    else:
        for i in range(num2,0,-2):
            dfac*=i
            sleep(0.2)
def Fibonacci():
    global fib, num3
    num = 1
    for i in range(num3-2):
        num,fib=fib,num+fib
        sleep(0.2)
fac=1
dfac=1
fib=1
num1=7
num2=7
num3=12
A=Thread(target=factorial)
B=Thread(target=double_factorial)
C=Thread(target=Fibonacci)
A.start()
B.start()
C.start()
A.join()
B.join()
C.join()
print("Results:")
print(f"Factorial of {num1} is {fac}")
print(f"Double factorial of {num2} is {dfac}")
print(f"{num3}-number in the Fibonacci sequence equal to {fib}")