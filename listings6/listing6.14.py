# Functions with recursive calls
# Function to calculate sum of numbers
def mysum(n):
    if n==0:
        return 0
    else:
        return n+mysum(n-1)
# Function to calculate Fibonacci numbers
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# Function for inverse displaying
def show(txt):
    if len(txt)==0:
        print("|")
    else:
        print("|", txt[-1], end="", sep="")
        show(txt[:-1])
# Call the functions
print("Sum of numbers:")
for k in range(12):
    print(mysum(k), end=" ")
print("\nFibonacci numbers:")
for k in range(15):
    print(fib(k+1), end=" ")
print("\nInverse text:")
show("Hello Python")
print("List inversion:")
show([1,2,3,4,5])