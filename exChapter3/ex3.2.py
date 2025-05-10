num=int(input("Enter an integer number: "))
tpl=()
while num>0:
    tpl+=(num%10,)
    num=num//10
print("Original tuple:", tpl[::-1])
print("Reversed tuple:", tpl)
