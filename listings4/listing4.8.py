text=input("The first text: ")
A=set(text)
text=input("The second text: ")
B=set(text)
C=A&B
print("Letters of the first text: ", A)
print("Letters of the second text: ", B)
print("Common letters: ", C)