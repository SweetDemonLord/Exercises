from threading import Thread
from time import sleep
# Derived class
class MyThread(Thread):
    def __init__(self,count,time,text):
        # Call of the base class constructor
        super().__init__()
        # Assigning values to the fields
        self.count = count
        self.time = time
        self.text = text
    # Method overriding for execution in a thread
    def run(self):
        for k in range(self.count):
            sleep(self.time)
            print("[",k+1,"]", self.text,sep="")
print("Program execution starts")
# Creating objects for child threads
A=MyThread(5,2,"Alpha")
B=MyThread(3,1.5,"Bravo")
# Starting a child thread for execution
A.start()
B.start()
# Waiting for child threads to finish
if A.is_alive():
    A.join()
if B.is_alive():
    B.join()
print("Program execution ends")