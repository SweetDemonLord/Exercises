text=input("Enter text: ")
print("Initial text: ")
L=text.split()
print(L)
lengths=[]
for k in L:
    lengths.append(len(k))
L.pop(lengths.index(max(lengths)))
L.pop(lengths.index(min(lengths)))
print(L)
print("Result: ", " ".join(L))