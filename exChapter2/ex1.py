number=input("Enter a number: ")
print("You have entered the number:",number)

for k in range(0,10):
    count = 0
    for i in range(0,len(number)):
        if(str(k)==number[i]):
            count+=1
    print("The digit",k,"appears in the number",count,"times.")