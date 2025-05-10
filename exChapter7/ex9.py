filename1=input("Enter a file name: ")
mf=open(filename1, encoding="utf-8")
txt=mf.read()
print("Contents of the file.")
print(txt)
txt=""
k=1
for line in mf:
    txt+=("["+str(k)+"]"+line)
    k+=1
filename2=filename1.replace(".txt","2.txt")
mf_copy=open(filename2,'w',encoding="utf-8")
mf_copy.write(txt)
mf.close()
mf_copy.close()
print("\nThe file is closed...")