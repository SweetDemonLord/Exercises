from threading import *
from time import sleep
def character_filling():
    global L1,last1
    ch='A'
    for i in range(last1):
        L1[i]=ch
        ch=chr(ord(ch)+1)
        sleep(0.2)
def numbers_filling():
    global L2,last2
    val=0
    for i in range(last2):
        L2[i]=val
        val+=77
        sleep(0.2)
size1=13
size2=7
L1=["*" for k1 in range(size1)]
L2=["*" for k2 in range(size2)]
last1=len(L1)
last2=len(L2)
C=Thread(target=character_filling)
N=Thread(target=numbers_filling)
C.start()
N.start()
C.join()
N.join()
print("Done")
print(L1)
print(L2)