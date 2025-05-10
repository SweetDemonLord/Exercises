from threading import Thread
from time import sleep
# Function for execution in child threads
def from_left():
    global first,last,L
    val=10
    while True:
        if first<last:
            L[first]=val
            first+=1
            sleep(0.3)
        else:
            break
def from_right():
    global first,last,L
    val="A"
    while True:
        if first<last:
            L[first]=val
            val=chr(ord(val)+1)
            last-=1
            sleep(0.3)
        else:
            break
size=11
L=["*" for k in range(size)]
first=0
last=len(L)-1
print("List before filling")
print(L)
A=Thread(target=from_left)
B=Thread(target=from_right)
A.start()
B.start()
A.join()
B.join()
print("List after filling")
print(L)