from random import *
def maxind(A):
    M=[k for k in range(2)]
    M[0]=max(A)
    M[1]=A.index(max(A))
    return M
seed(2024)
nums=[randint(0,100) for i in range(10)]
print("Maximum value of the list and its index:", maxind(nums))