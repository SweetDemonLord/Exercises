from threading import Thread
from time import sleep
# Function with three arguments
def display(count,time,text):
    for k in range(count):
        # Pause in thread execution
        sleep(time)
        print("[",k+1,"] ",text,sep="")
print("Program execution starts")
# Creating a child thread object
t=Thread(target=display, args=(5,2,"Child thread"))
# Starting the child thread for execution
t.start()
# Calling a function in the main thread
display(3,1.5,"Main thread")
# Waiting for the child thread to complete
t.join()
print("Program execution ends")