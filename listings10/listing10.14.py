from threading import *
from time import sleep
# Function to be executed in a thread
def display(txt):
    A=[1,2]
    B=["A","B"]
    sleep(1)
    # Waiting for the flag to be set
    myevent.wait()
    # Canceling the flag setting
    myevent.clear()
    for a in A:
        print("[",a,"] ",txt,sep="")
    # Setting the flag
    myevent.set()
    sleep(1)
    # Waiting for the flag to be set
    myevent.wait()
    # Canceling the flag setting
    myevent.clear()
    for b in B:
        print("[",b,"] ",txt,sep="")
    # Setting the flag
    myevent.set()
# Creating an object
myevent=Event()
# Setting the flag
myevent.set()
# Objects of child threads
F=Thread(target=display,args=["First"])
S=Thread(target=display,args=["Second"])
# Starting child threads
F.start()
S.start()
# Waiting for child threads to finish
F.join()
S.join()