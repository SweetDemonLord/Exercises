stars="{0:{2}{1}s}"
length=9
for s in range(1,length+1):
    print(stars.format("*", length+1-s, ">"), end="")
    if (s!=int(length/2+1) and s!=1):
        print(" "*(2*s-1),end="")
    else:
        print("-"*(2*s-1),end="")
    print(stars.format("*", length+1+s, "<"))