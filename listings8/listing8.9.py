from copy import *
class MyClass:
    pass
A=MyClass()
A.value=100
A.nums=[1,2,3]
B=A
C=copy(A)
D=deepcopy(A)
print("Object are created")

print("A:",A.value,"and",A.nums)
print("B:",B.value,"and",B.nums)
print("C:",C.value,"and",C.nums)
print("D:",D.value,"and",D.nums)
print("A.value=200 and A.nums[1]=0")
A.value=200
A.nums[1]=0
print("A:",A.value,"and",A.nums)
print("B:",B.value,"and",B.nums)
print("C:",C.value,"and",C.nums)
print("D:",D.value,"and",D.nums)
print("A is deleted")
del A
print("B.value=300 and B.nums[2]=4")
B.value=300
B.nums[2]=4
print("B:",B.value,"and",B.nums)
print("C:",C.value,"and",C.nums)
print("D:",D.value,"and",D.nums)