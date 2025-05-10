def only_odd(l1):
    l2=[]
    for k in range(len(l1)):
        if l1[k]%2==1:
            l2.append(l1[k])
    return l2
L=eval(input("Enter a list: "))
L=only_odd(L)
print("The result: ", L)