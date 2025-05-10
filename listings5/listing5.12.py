txt=input("Enter text: ")
new_txt=""
m=ord("a")
n=ord("z")
M=ord("A")
N=ord("Z")
for s in txt:
    k=ord(s)
    if (k>=m and k<n) or (k>=M and k<N):
        s=chr(k+1)
    elif k==n:
        s=chr(m)
    elif k==N:
        s=chr(M)
    new_txt+=s
print("Cipher: ", new_txt)