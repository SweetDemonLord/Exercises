# Connecting functions to generate random numbers
from random import *
# Initialization random numbers generating
seed(2024)
# A number of different random numbers
count=10
# Creating an empty set
nums=set()
# Generating random numbers
while len(nums)<count:
    nums.add(randint(1,count+5))
# Displaying the result
print(nums)