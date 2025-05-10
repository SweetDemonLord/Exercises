def recursion(txt):
    if (len(txt)!=0):
        print(txt[0], end="")
        recursion(txt[2:])
text=input("Enter text: ")
recursion(text)