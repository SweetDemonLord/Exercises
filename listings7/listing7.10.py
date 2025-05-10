# Open text file for reading
mf=open("D:\\Programming\\Python\\listings\\listings7\\poetry.txt",
        encoding="utf8")
# Variable for line numbering
k=1
# Reading a file line by line
print("Reading a file line by line")
for L in mf:
    print("["+str(k)+"]",L,end="")
    k=k+1
mf.close()
print("\nThe file is closed...")

k=1
print("Reading a file line by line")
with open("D:\\Programming\\Python\\listings\\listings7\\poetry.txt",
          encoding="utf8") as fm:
    for L in fm:
        print("["+str(k)+"]",L,end="")
        k=k+1
print("\nThe file is closed...")