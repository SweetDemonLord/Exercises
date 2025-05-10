print("Numbers are given in different number systems:")
# 19 number in binary
A=0b10011
print("A =", A)
# 93 number in octal
B=0o135
print("B =", B)
# 2603 number in hexadecimal
C=0xA2B
print("C =", C)
print("C-A-B =", C-A-B)
# Inverse transformation
print("Inverse transformation:")
A=int("10011",2)
print(bin(A),"=",A)
B=int("0o135",8)
print(bin(B),"=",B)
C=int("0xA2B",16)
print(hex(C),"=",C)
D=int("ABC",20)
print("ABC =", D)