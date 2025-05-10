base=int(input("Enter a base of a number system: "))
num=eval(input("Enter a number: "))
if base==2:
    print(num,"=",bin(num))
elif base==8:
    print(num,"=",oct(num))
elif base==16:
    print(num,"=",hex(num))
else:
    print("Wrong input of the base of a number")