from threading import *
mylock=BoundedSemaphore(5)
num=int(input("Enter an integer number: "))
for k in range(num):
    mylock.acquire()
    print(k+1, end=" ")
for k in range(num):
    mylock.release()