num=int(input("Enter a number: "))
bits=int(input("Enter a bit number: "))
one=1
print(num,"=",bin(num))
if bool(num & one<<bits-1):
    print(f"Entered bit №{bits} is 1")
else:
    print(f"Entered bit №{bits} is 0")