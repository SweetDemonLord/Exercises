from random import *
seed(2024)
nums=[randint(0,100) for i in range(20)]
print("The original list:",nums)
cut=nums[1:len(nums)-1]
for i in range(1,len(cut)+1):
    cut[i-1]=nums[i-1]+nums[i+1]
for i in range(1,len(nums)-1):
    nums.pop(i)
    nums.insert(i,cut[i-1])
print("Result:",nums)
