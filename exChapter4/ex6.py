num=int(input("Enter an integer positive number: "))
while num<0:
    num=int(input("Please enter a positive number: "))
nums=[k for k in range(1,num+1)]
ndict={nums[k]: nums[len(nums)-k-1] for k in range(len(nums))}
print(ndict)