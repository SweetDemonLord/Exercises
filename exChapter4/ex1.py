from random import *
seed(2024)
nums={randint(1,10) if k<5 else randint(10,30) for k in range(1,15)}
print("Random 15 numbers.")
print("The first 5 numbers in range 1-10. The remaining 10 numbers in range 10-3")
print(nums)
