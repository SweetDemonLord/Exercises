filename=input("Enter a file name: ")
txt=input("Enter text: ")
mf=open(filename,'w',encoding='utf-8')
text=''
for ch in txt:
    if ch.islower():
        ch=ch.upper()
    text+=ch
mf.write(text)
