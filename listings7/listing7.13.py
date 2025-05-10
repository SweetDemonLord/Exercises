name="D:\\Programming\\Python\\listings\\listings7\\mydata.txt"
txt="Python"
print("Text of the writing in the file:")
mf=open(name,"w+t")
mf.write(txt)
mf.seek(0)
print(mf.tell(),"->",mf.read(1))
num=mf.tell()-1
mf.seek(num)
print("mf.tell()","->",mf.read(1))
mf.seek(0)
print("Three characters:", mf.read(3))
mf.close()
print("The program has completed execution.")
