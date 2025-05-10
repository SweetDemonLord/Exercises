# A new list is entered
nums=eval(input("Enter a list: "))
# An upper limit is entered
limit=int(input("Enter a limit: "))
the_sum=0
for i in range(limit+1):
    the_sum+=i
the_sum-=sum(nums)
print("The sum of",limit,"number besides the list element is:",the_sum)