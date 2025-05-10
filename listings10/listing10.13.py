from threading import *
from time import sleep
# Function in a thread for execution
def calc(txt, op):
    # Global variable
    global number
    # Cycle operator
    for k in range(3):
        # Blocking resources
        mylock.acquire()
        print(txt,": resource is blocked", sep="")
        # Controlled code
        try:
            # Reading a value of a variable
            print(txt,"is read:",number)
            # The value of the variable is memorized
            val=number
            # Pause in the execution of the thread
            sleep(1)
            # Changing the variable of the value
            if op:
                number=val+1
            else:
                number=val-1
            # Displaying the value of the variable
            print(txt,"is written:",number)
        finally:
            print(txt,": resource is unblocked", sep="")
            print("--------------------------------")
            # Unblocking resource
            mylock.release()
        # Pause in the execution of the thread
        sleep(1)
# Starting value of the global variable
number=0
# Lock object
mylock=Lock()
# Object of the child threads
A=Thread(target=calc, args=["A", True])
B=Thread(target=calc, args=["B", False])
# Starting child threads for execution
A.start()
B.start()
# Waiting for threads to finish
A.join()
B.join()