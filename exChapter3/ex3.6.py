from random import *
seed(2024)
nums=[randint(0,100) for i in range(10)]
print("The original list:",nums)
count=len(nums)-1
while count>0:
    for i in range(count):
        if(nums[i]>nums[i+1]):
            nums[i],nums[i+1]=nums[i+1],nums[i]
    count-=1
print("The sorted list by bubble method:",nums)