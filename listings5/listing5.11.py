txt=input("Enter text: ")
new_txt=""
num=0
while num<len(txt)-1:
    new_txt+=txt[num+1]+txt[num]
    num+=2
if num<len(txt):
    new_txt+=txt[num]
print("Result:", new_txt)