from random import *
seed(2024)
nums=[randint(0,100) for i in range(20)]
print("The original list:", nums)
enums=nums[0:100:2]
nums=nums[1:100:2]
enums=sorted(enums)
nums=sorted(nums)
print("The sorted list:", nums)
print("Enums:", enums)
for i in range(20):
    if i%2==0:
        nums.insert(i,enums[i//2])
print("Result:", nums)