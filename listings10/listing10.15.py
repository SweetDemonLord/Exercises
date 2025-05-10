from threading import *
from time import sleep
# Function to be called in a thread
def mysum():
    global num
    k=1
    txt=str(num)
    while myevent.is_set():
        num+=k
        txt+=" + "+str(k)
        print("[",k,"] ",txt," = ", num, sep="")
        k+=1
        sleep(0.3)
print("Sum of integers")
t=Thread(target=mysum)
num=0
# Object for thread synchronization
myevent=Event()
# Setting the flag
myevent.set()
t.start()
sleep(2)
myevent.clear()
if t.is_alive():
    t.join()
print("Result:",num)