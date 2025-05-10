txt=input("Enter text: ")
txt=txt.lower()
# Conversion result
print(txt)
# Splitting text into substrings
L=txt.split(" ")
# Splitting result
print(L)
s=0
n=0
# Looping through list elements
for k in range(len(L)):
    # Stripping non-letter character
    w=L[k].strip(".,:;-!?")
    # If text is not empty
    if len(w)!=0:
        # Displaying a word and its length
        print(w.ljust(12),"-",len(w))
        # Sum of letters at words
        s+=len(w)
        # A number of words
        n+=1
# The average value
s/=n
# Result of calculations
print("The average length is ",s)
