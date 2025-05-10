def pairwise_product(l1, l2):
    s=0
    if len(l1) >= len(l2):
        for k in range(len(l2)):
            s+=l1[k]*l2[k]
        for k in range(len(l1)-len(l2)):
            s+=l1[len(l2)+k]*l2[k]
    else:
        for k in range(len(l1)):
            s += l1[k] * l2[k]
        for k in range(len(l2) - len(l1)):
            s += l2[len(l1) + k] * l1[k]
    return s
L1=eval(input("Enter the first list: "))
L2=eval(input("Enter the second list: "))
print("The result:", pairwise_product(L1,L2))