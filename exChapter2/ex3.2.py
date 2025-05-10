nums=[12,3,456,789]
print("Initial list:",nums)
number=0
i = 0
for k in range (len(nums)):
    number=number+nums[len(nums)-1-k]*10**i
    num = nums[len(nums)-1-k]
    while num>0:
        num=num//10
        i+=1

print("Result:",number)