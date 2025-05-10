nums=[12,3,456,78]
print("Initial list:",nums)
number=0
for k in range (len(nums)):
    i = 0
    num = nums[k]
    while num>0:
        num=num//10
        i+=1
    number=number*10**i+nums[k]
print("Result:",number)