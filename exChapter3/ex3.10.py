list1,list2=[2**k for k in range(10)],[3**k for k in range(10)]
print("The first list:",list1)
print("The second list:",list2)
list3=[]
for i in range(len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])
print("The first and second lists are alternately connected:")
print(list3)