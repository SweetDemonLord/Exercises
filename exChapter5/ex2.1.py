stars="{0:{2}{1}s}"
length=9
for s in range(1,length+1):
    if(s!=1):
        print(stars.format("*", length+2-s, ">"), end="")
        if (s!=int(length/2+1)):
            print(" "*(2*s-3),end="")
        else:
            print("-"*(2*s-3),end="")
        print(stars.format("*", length+2+s, "<"))
    else:
        print(stars.format("*", 2*length+1, "^"))