number=int(input("Enter a number: "))
k=1
while k<=number//2:
    if number%k==0:
        print("Divisible by", k)
    k=k+1
print("Divisible by", number)