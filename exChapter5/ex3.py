text=input("Enter text: ")
delta=ord('a')-ord('A')

print("Initial text: ", text)
swap_txt=""
for s in text:
    if(ord(s)>=ord('A') and ord(s)<=ord('Z')):
        s=chr(ord(s)+delta)
    elif(ord(s)>=ord('a') and ord(s)<=ord('z')):
        s=chr(ord(s)-delta)
    swap_txt+=s
print("After swapping: ",swap_txt)