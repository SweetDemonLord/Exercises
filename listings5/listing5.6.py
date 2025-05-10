txt=input("Enter text: ")
symb=input("Which letter to find? ")
num=txt.count(symb)
if num==0:
    print("There is no letter in text!")
else:
    print(f"Text have {num} letters '{symb}'.")