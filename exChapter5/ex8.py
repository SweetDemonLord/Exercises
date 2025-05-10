txt=input("Enter text: ")
encryption=""
vowers=['a','e','o','i','u','y','A','E','O','I','U','Y']
consonants=['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m'
            'Q','W','R','T','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
# Encryption
for s in txt:
    if (set(s)&set(vowers)):
        s=chr(ord(s)+1)
    elif(set(s)&set(consonants)):
        s = chr(ord(s)+1)
        if s=='z':
            s='a'
        if s=='Z':
            s='A'
    encryption += s
print("Cipher: ", encryption)
# Transcript
transcript=""
for s in encryption:
    if (set(s) & set(consonants)):
        s = chr(ord(s)-1)
    elif (set(s) & set(vowers)):
        s=chr(ord(s)-1)
        if s == 'a':
            s='z'
        if s == 'A':
            s='Z'
    transcript+=s
print("Transcript: ", transcript)