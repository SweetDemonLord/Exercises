from fractions import Fraction
a,b=eval(input("Enter a real and imaginary of the first complex number: "))
complex1=complex(a,b)
a,b=eval(input("Enter a real and imaginary of the second complex number: "))
complex2=complex(a,b)
print("Product of the complex numbers: ", complex1*complex2)
print("Sum of the complex numbers: ", complex1+complex2)
print("Quotient of the complex numbers: ", complex1/complex2)
L=[abs(complex1*complex2),abs(complex1+complex2),abs(complex1/complex2)]
print("Maximum value of three operations: ", max(L))
print("Minimum value of three operations: ", min(L))