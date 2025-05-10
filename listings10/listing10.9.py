# Import of Thread class
from threading import Thread
# Import of sleep() function
from time import sleep
# Function to be called in the main thread
def alpha():
    for k in range(5):
        # Pause in thread execution
        sleep(0.33)
        print("[",k+1,"] Alpha", sep="")
# Function to be executed in the child thread
def bravo():
    for k in range(5):
        print("[",k+1,"] Bravo", sep="")
        # Pause in thread execution
        sleep(0.66)
# Creating a child thread object
t=Thread(target=bravo)
# Starting a child thread for execution
t.start()
# Calling a function in the main thread
alpha()