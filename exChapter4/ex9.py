# 0.9 Из-за Васильева
text=input("Enter text: ")
dictionary={}
for char in text:
    if char not in dictionary:
        txt=list(text)
        for i in range(len(txt)):
            if txt[i]==char:
                txt.pop(i)
                break
        dictionary[char]=txt

for key, word in dictionary.items():
    print(f"{key} : {word}")
# 1
text=input("Enter text: ")
dictionary={}
for char in text:
    new_text=text.replace(char,"")  # Cross out a symbol from the text
    if char not in dictionary:
        dictionary[char]=new_text         # Adding as a key with the new text as the value
for key,value in dictionary.items():
    print(f"{key} : {value}")