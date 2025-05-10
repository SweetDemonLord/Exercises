number=int(input("Enter a number: "))
print("You have entered the number:",number)

for k in range(0,10):
    num = number
    count = 0
    while num>0:
        digit=num%10
        if (digit==k):
            count+=1
        num=num//10
    print("The digit",k,"appears in the number",count,"times.")

number2=int(input("Enter a number: "))
print("You have entered the number:",number2)
while number2>0:
    digit=number2%10
    print("The digit",digit, "appears in the number.")
    number2=number2//10
