#1
text=input("Enter text: ")
dictionary={}
for char in text:
    if char in dictionary:
        dictionary[char]+=1
    else:
        dictionary[char]=1
print(dictionary)
#2
text=input("Enter text: ")
dictionary={}
for char in text:
    if char not in dictionary:
        dictionary[char]=text.count(char)
print(dictionary)