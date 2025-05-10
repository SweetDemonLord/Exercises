from threading import *
from time import sleep
def mysum(n, N):
    res=0
    for k in range(N+1):
        res+=k**n
        sleep(0.1)
    return res
def display(n,N):
    # Locking the locking object
    mylock.acquire()
    # Getting a reference to the current thread
    t=current_thread()
    # Displaying a name of the thread
    print("Thread:",t.name)
    print("Constituents:", N)
    print("Degree:", n)
    print("Sum:",mysum(n,N))
    print("------------------")
    mylock.release()
mylock = Lock()
names=["Alpha","Bravo","Charlie","Delta"]
T=[Thread(target=display,args=[k+1,10],name=names[k]) for k in range(len(names))]
for t in T:
    t.start()
for t in T:
    t.join()