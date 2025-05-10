def text_result(txt,*n):
    letters=txt.strip(",.!?:;_-=+#@")
    txt=""
    for letter in letters:
        if letter.isalpha():
            txt+=letter
    result = []
    for i in n:
        if i>len(txt)-1:
            i=len(txt)-1
        elif i<0:
            i=0
        result.append(txt[i])
    return "".join(result)
text=input("Enter text: ")
print("Text-result:",text_result(text, 2,4,5,8))