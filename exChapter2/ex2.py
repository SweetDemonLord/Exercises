number=int(input("Enter an integer number: "))
print("You have entered the number:",number)
complement=0
while number>0:
    digit=number%10
    complement=complement*10+(9-digit)
    number=number//10
print("Reversed number:",complement)