mf=open("D:\\Programming\\Python\\listings\\listings7\\poetry.txt",
        encoding="utf8")
k=1
print("Reading a file line by line")
L=mf.readline()
while L!="":
    print("["+str(k)+"] ",end="")
    for s in L:
        if s==' ':
            s='_'
        print(s, end="")
    k+=1
    L=mf.readline()
mf.close()
print("\nThe file is closed...")