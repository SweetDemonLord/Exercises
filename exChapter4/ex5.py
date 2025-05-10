nums=set()
count=1
while count<20:
    nums.add((count,count+2))
    count+=2
print(sorted(nums))