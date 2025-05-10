from threading import Thread
from time import sleep
# Class for creating a callable object
class MyClass:
    def __init__(self, text):
        self.text=text
    # The method is called when the object is called
    def __call__(self,count,time):
        for k in range(count):
            sleep(time)
            print("[", k+1, "] ",self.text, sep="")
print("Program execution starts")
# Creating a called object
obj=MyClass("Child thread")
# Creating an objet of the child thread
t=Thread(target=obj, kwargs={"time":2,"count":5})
# Starting a child thread for execution
t.start()
# Calling an anonymous object in the main thread
MyClass("Main thread")(3,1.5)
# Waiting for child thread to finish
if t.is_alive():
    t.join()
print("Program execution ends")