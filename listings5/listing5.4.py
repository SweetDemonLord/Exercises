txt="Hello Python"
print(txt)
A=txt[::-1]
print(A)
B=txt[:5]
C=txt[6:]
print(C)
new_txt=""
delta=ord("a")-ord("A")
for s in txt:
    # If a letter is in the range from a to z
    if(ord(s)>=ord("a") and ord(s)<=ord("z")):
        s=chr(ord(s)-delta)
    new_txt+=s
print(new_txt)