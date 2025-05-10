from fractions import Fraction
a,b=eval(input("Enter a numerator and denominator of the first fraction: "))
fraction1=Fraction(a,b)
a,b=eval(input("Enter a numerator and denominator of the second fraction: "))
fraction2=Fraction(a,b)
print("Product of the fractions: ", fraction1*fraction2)
print("Sum of the fractions: ", fraction1+fraction2)
print("Quotient of the fractions: ", fraction1/fraction2)
L=[fraction1*fraction2,fraction1+fraction2,fraction1/fraction2]
print("Maximum value of three operations: ", max(L))
print("Minimum value of three operations: ", min(L))