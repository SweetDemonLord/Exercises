from threading import *
from time import sleep
def display(lst):
    mylock.acquire()
    t=current_thread()
    print("Thread:",t.name)
    print(lst)
    sleep(0.2)
    print("-----------------------")
    mylock.release()
mylock = Lock()
names=["Alpha","Bravo","Charlie","Delta"]
students=[["Insaf","Samir","Bax"],["Ins","Sam","Bx"],["Joker","Batman","Superman"],["Car","House","Wife"]]
T=[Thread(target=display,args=[students[k]],name=names[k])
   for k in range(len(names))]
for t in T:
    t.start()
for t in T:
    t.join()