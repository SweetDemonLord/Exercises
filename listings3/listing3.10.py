# Size of a list
n=10
# Initial value of the list
A=[1,1]
for k in range(n-2):
    A.append(A[-1]+A[-2])
# Checking contents of the list:
print("A:", A)
# Changing the order of items in the list
for k in range(len(A)-1):
    A.append(A.pop(-k-2))
# Checking contents of the list
print("A:", A)
# Removing the greatest item in the list
A.remove(max(A))
# Checking contents of the list
print("A:", A)
# Removing the smallest item in the list
A.remove(min(A))
# Checking contents of the list
print("A:", A)
# Adding an item at the beginning of the list
A.insert(0, A[0]+A[1])
# Checking contents of the list
print("A:", A)
# The empty list
B=[]
# Some items of one list are transferred to another
for k in range(len(A)//2):
    B.insert(0, A.pop(-1))
# Checking contents of the lists
print("A:", A)
print("B:", B)
# Appending an item to the end of the list
A.append(B)
# Checking contents of the list
print("A:", A)
# Removing the last item in the list
A.pop(-1)
# Checking contents of the list
print("A:", A)
# Adding an item in the list
A.extend(B)
# Checking contents of the list
print("A:", A)
A.sort()
print("A:", A)
print("Index of the maximum item in the list: ", A.index(max(A)))