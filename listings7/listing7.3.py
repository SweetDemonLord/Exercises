from fractions import Fraction
from decimal import Decimal
print("Fractional value:")
A=Fraction(2,5)
print("A =", A)
B=Fraction(3,7)
print("B =", B)
C=A+B
print("A+B =", C)
print("Real numbers:")
x=2/5
print("x =", x)
D=x+B
print("x+B =", D)
print("Number of specified precision:")
A=Decimal('1.01')
print("A =", A)
B=Decimal('2.02')
print("B =", B)
C=A+B
print("A+B =", C)
print("1.01+2.02 =",1.01+2.02)