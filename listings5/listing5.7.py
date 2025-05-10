txt=input("Enter text: ")
symb=input("Which letter to find? ")
num=txt.find(symb)
L=[]
while num!= -1:
    L.append(num)
    num=txt.find(symb,num+1)
if len(L)==0:
    print("There is no such letter in the text!")
else:
    print(f"The position of the letter '{symb}' in the text is: {L}")