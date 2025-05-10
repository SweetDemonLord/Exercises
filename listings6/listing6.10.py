# The function uses global
# and local variables
def myfunction():
    # Global variables
    global A, B
    # Assigning values to variables
    A="Альфа"
    B="Браво"
    D="Дельта"
    # Checking values
    print("In the function: A =", A)
    print("In the function: B =", B)
    print("In the function: C =", C)
    print("In the function: D =", D)
A="Alpha"
C="Charlie"
D="Delta"
# Checking variables values
print('Before calling the function: A =',A)
print("Before calling the function: C =",C)
print("Before calling the function: D =",D)
# Calling the function
myfunction()
# Checking variables values
print("After calling the function: A =",A)
print("After calling the function: B =",B)
print("After calling the function: C =",C)
print("After calling the function: D =",D)