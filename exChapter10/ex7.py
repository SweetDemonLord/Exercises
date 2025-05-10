from threading import Thread
from time import sleep
def odd_index():
    global L, last
    val=7
    for i in range(last):
        if i % 2 == 1:
            L[i]=val
            val+=7
            sleep(0.2)
def even_index():
    global L, last
    val="A"
    for i in range(last):
        if i % 2 == 0:
            L[i]=val
            val=chr(ord(val)+1)
            sleep(0.2)
size=14
L=["*" for k in range(size)]
last=len(L)
A=Thread(target=even_index)
B=Thread(target=odd_index)
A.start()
B.start()
A.join()
B.join()
print("Done")
print(L)