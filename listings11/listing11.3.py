from tkinter import *
# Function for handling a press of a button
def clicked():
    global t
    # Reading contents of the text field
    t=txt.get()
    # Closing the window
    wnd.destroy()
# Create an object for the first window
wnd=Tk()
# Window parameters
wnd.title("Let's be acquainted")
wnd.geometry("300x120")
wnd.resizable(False,False)
# Fonts
fnt_1=("Arial",13,"bold")
fnt_2=("Arial",13,"italic")
fnt_3=("Arial",10,"bold")
# Variable for reading text from the input field
t=""
# Creating an object for text label
lbl=Label(master=wnd,text="What's your name?")
# Font for the label
lbl.configure(font=fnt_1)
# Adding the label in the window
lbl.place(x=10,y=20)
# Creating an object for input field
txt=Entry(master=wnd,width=30)
# Font for the input field
txt.configure(font=fnt_2)
# Placing text field in the window
txt.place(x=10,y=50)
# Creating objects for buttons
btn_1=Button(master=wnd,text="OK")
btn_2=Button(master=wnd,text="Cancel")
# Parameters of the buttons
btn_1.configure(font=fnt_3)
btn_1.configure(command=clicked)
btn_2.configure(font=fnt_3)
btn_2.configure(command=wnd.destroy)
# Placing the buttons in the window
btn_1.place(x=40,y=80,width=100,height=30)
btn_2.place(x=150,y=80,width=100,height=30)
# Displaying the first window on the screen
wnd.mainloop()
# If the user entered text
if t!="":
    # Creating an object for the second window
    msg=Tk()
    # Parameters of the second window
    msg.title("The acquaintance has been completed")
    msg.geometry("320x100")
    msg.resizable(False,False)
    # Label with a message for the second window
    lbl=Label(master=msg, text="Very kindly, "+t+"!", relief=SUNKEN)
    # Font for the label
    lbl.configure(font=fnt_1)
    # Placing the label in the second window
    lbl.place(x=10,y=10,height=40,width=300)
    # Button object creation
    btn=Button(master=msg, text="OK")
    # Font for the button
    btn.configure(font=fnt_3)
    # Method for handling a press of a button
    btn.configure(command=msg.destroy)
    # Placing the button in the second window
    btn.place(x=110,y=60,width=100,height=30)
    # Displaying the second window on the screen
    msg.mainloop()