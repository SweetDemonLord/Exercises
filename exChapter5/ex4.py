text=input("Enter text: ")
new_text=""
k=0
while k<len(text)-2:
    new_text+=text[k+2]+text[k+1]+text[k]
    k+=3
if k<len(text):
    new_text+=text[k]+text[k+1]
print("Result:",new_text)