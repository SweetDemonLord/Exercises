# Class import from a package
from tkinter import *
# Class import from a subpackage
from tkinter.ttk import Combobox
# Function for handling an event related
# to selecting an item in a dropdown list
def change(evt):
    # Reading the value selected in the list
    t=cb.get()
    # Determining the image based on the selected value
    for k in range(len(names)):
        # If the selected value matches
        # the text in the list
        if t==names[k]:
            # A new image in the label
            lbl.configure(image=imgs[k])
            # Termination of the loop statement
            break
# A variable with the path to image files
path="D:\\Programming\\Python\\Pictures\\"
# Names of animals
names=["Tiger","Lion","Bax","Irbis"]
files=["tiger.png","lion.png","звой.png","irbis.png"]
# Creating a window object
wnd=Tk()
# Parameters of the window
wnd.title("Predators")
wnd.geometry("220x300")
wnd.resizable(False,False)
# A list of objects for images
imgs=[PhotoImage(file=path+f) for f in files]
# Index for the initially selected item
index=2
# Creating a label object
lbl=Label(wnd,image=imgs[index])
# Label parameters and its placement in the window
lbl.configure(relief=GROOVE)
lbl.place(x=10,y=10, width=200, height=200)
# Creating an object for the drop-down list
cb=Combobox(wnd, state="readonly")
# Contents of the drop-down list
cb.configure(values=names)
# The initially selected value (item)
cb.current(index)
# Font for the drop-down list
cb.configure(font=("Arial",11,"bold"))
# Defining an event handler
# for selecting a new value in the list
cb.bind("<<ComboboxSelected>>",change)
# Placing the list in the window
cb.place(x=10,y=220,width=200,height=30)
# Creating a button object
btn=Button(wnd,text="OK")
# Defining a handler
# for the button click event
btn.configure(command=wnd.destroy)
# Button size and its placement in the window
btn.place(x=60,y=260,width=100,height=30)
# Displaying the window on the screen
wnd.mainloop()