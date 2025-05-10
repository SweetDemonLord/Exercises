# The first dictionary
nums={100:"hundred",1:"unit",10:"ten"}
print(nums)
print("1: ", nums[1])
print("10: ", nums[10])
print("100: ", nums[100])
# Dictionary operations
nums[3]="troika"
nums[10]="ten"
nums.pop(100)
print(nums)
# The second dictionary
order=dict(First=1, Third=3, Last=10)
print(order)
print("First:", order["First"])
print("Third:", order["Third"])
print("Last: ", order["Last"])
# Dictionary operations
order["Last"]=12
del order["Third"]
order["Fifth"]=5
print(order)
