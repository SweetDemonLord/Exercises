decimal_number=int(input("Enter a decimal number: "))
octal_number=oct(decimal_number)[2:]
reversed_octal_number=octal_number[::-1]
print(f"Number {decimal_number} in the octal system with reversed numbers: {reversed_octal_number}")
