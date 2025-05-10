txt=input("Enter text: ")
encryption=""
m=ord("a")
n=ord("z")
M=ord("A")
N=ord("Z")
# Encryption
for s in txt:
    k=ord(s)
    if (k>m and k<n) or (k>M and k<N):
        s=chr(k-2)
    elif k==n:
        s=chr(m)
    elif k==N:
        s=chr(M)
    elif k==m:
        s=chr(n)
    elif k==M:
        s=chr(N)
    encryption+=s
print("Cipher: ", encryption)
# Transcript
transcript=""
for s in encryption:
    k=ord(s)
    if (k>m and k<n) or (k>M and k<N):
        s=chr(k+2)
    elif k == n:
        s = chr(m)
    elif k == N:
        s = chr(M)
    elif k==m:
        s=chr(n)
    elif k==M:
        s=chr(N)
    transcript+=s
print("Transcript: ", transcript)