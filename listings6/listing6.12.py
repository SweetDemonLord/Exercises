num=10
# Function based on lambda expression
L=lambda n: 2*n+1
# Checking result
print("Odd numbers:")
for k in range(num):
    print(L(k), end=" ")
# A new value
L=lambda n: 2**n
# Checking result
print("\nPowers of two:")
for k in range(num):
    print(L(k), end=" ")
# Direct call lambda-function
print("\nSquares of numbers:")
for k in range(num):
    print((lambda x: x*x)(k+1), end=" ")
# Normal function
def calc(x,y):
    return x+y
# Using function in a lambda-expression
F=lambda x,y: calc(x,y)
# Variable is assigned a name of the function
fac=calc
# The name of the function is assigned lambda-expression
calc=lambda x,y: x*y
# Checking results
print("\nCall F(3,5):", F(3,5))
print("Call f(3,5):", fac(3, 5))
print("Call calc(3,5):", calc(3,5))