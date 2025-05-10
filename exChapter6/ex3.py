def avg_max_min(*n):
    l=[]
    for i in n:
        l.append(i)
    amm=[]
    amm.append(sum(l)//len(l))
    amm.append(max(l))
    amm.append(min(l))
    return amm
print("Average, maximum and minimum values of arguments accordingly: ",
      avg_max_min(10,20,30,40,50))
