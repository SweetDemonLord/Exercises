num=int(input("Enter a number: "))
txt=oct(num)
num=''
for ch in range(2, len(txt)):
    num+=txt[ch]
print("Initial number in the octal number system",num)
print("Initial number is reversed in the octal number system",num[::-1])