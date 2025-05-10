# Class import from a package
from tkinter import *
# Window object creation
wnd=Tk()
# Title for the window
wnd.title("Window with a button")
# Geometric dimensions of the window
wnd.geometry("250x150")
# Window with fixed dimensions
wnd.resizable(False,False)
# Creating a label object
lbl=Label(wnd, text="Hello everyone!", font=("Arial Bold",20))
# Placing the label in the window
lbl.place(x=40,y=30)
# Button object
btn=Button(wnd, text="Close", font=("Courier New Bold",13), command=wnd.destroy)
# Placing the button object in the window
btn.place(x=40,y=100, width=170, height=30)
# Displaying the window on the screen
wnd.mainloop()