text1=input("Enter the first text: ")
text2=input("Enter the second text: ")
new_text=""
text1,text2=text1+'*',text2+'*'
print(text1)
print(text2)
for k in text1:
    new_text=new_text+k
for k in text2:
    new_text=new_text+k

print("Result: ", new_text)