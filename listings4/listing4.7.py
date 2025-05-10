number=int(input("Enter a number: "))
if number<0:
    number*=-1
digits=set()
if number==0:
    digits.add(0)
else:
    while number!=0:
        digits.add(number%10)
        # The last digit is dropped when
        # representing a number
        number=number//10
print("The number consists of such digits:")
for n in digits:
    print(n, end=" ")
# Go to a new line
print()