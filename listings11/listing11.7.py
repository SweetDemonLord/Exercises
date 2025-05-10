from tkinter import *
from math import *
# Function for handling the event related to hovering the
# cursor over the drawing area
def msEnter(evt):
    # Image change
    cnv.itemconfig(Pct, image=img_2)
# Function for handling the event when
# the cursor leaves the drawing area
def msLeave(evt):
    # Image change
    cnv.itemconfig(Pct, image=img_1)
    # Delete "old" lines near the cursor
    cnv.delete("ln")
# Function for handling the event related
# to moving the cursor in the drawing area
def msMotion(evt):
    # Coordinates of the cursor in the drawing area
    x=evt.x
    y=evt.y
    # Delete "old" lines
    cnv.delete("ln")
    # Displaying lines
    cnv.create_line(x,5, x, H-5, fill=clr_C1, width=2, tag="ln")
    cnv.create_line(5, y, W-5, y, fill=clr_C1, width=2, tag="ln")
    # Rectangle coordinates
    Rxy=cnv.coords(Rtn)
    # Circle coordinates
    Cxy=cnv.coords(Crl)
    # Circle center coordinates
    x0=(Cxy[2]+Cxy[0])/2
    y0=(Cxy[3]+Cxy[1])/2
    # Distance from the cursor to the center of the circle
    r=sqrt((x-x0)**2+(y-y0)**2)
    # If the cursor is inside the circle
    if r<R:
        # White fill color for the circle
        cnv.itemconfig(Crl, fill=clr_C2)
        # Red fill color for the rectangle
        cnv.itemconfig(Rtn, fill=clr_C1)
        # Completing the function execution
        return
    # If the cursor is out the circle
    else:
        # Red fill color for the circle
        cnv.itemconfig(Crl, fill=clr_C1)
    # If the cursor is inside the rectangle
    if x>Rxy[0] and x<Rxy[2] and y>Rxy[1] and y<Rxy[3]:
        # Green fill color for the rectangle
        cnv.itemconfig(Rtn, fill=clr_R2)
    # If the cursor is out the rectangle
    else:
        # White fill color for the rectangle
        cnv.itemconfig(Rtn, fill=clr_R1)
# Function for handling the event related
# with pressing "up" button
def msUp(evt):
    # Group of lines is shifted up by one pixel
    cnv.move("Lns",0,-1)
    # The circle is shifted down by three pixels
    cnv.move(Crl,0,3)
# Function for handling the event related
# with pressing "down" button
def msDown(evt):
    # Group of lines is shifted down by one pixel
    cnv.move("Lns",0,1)
    # The circle is shifted up by three pixels
    cnv.move(Crl,0,-3)
# Function for handling the event related
# with pressing "left" button
def msLeft(evt):
    # Text is shifted left by one position
    cnv.move(Txt,-5,0)
# Function for handling the event related
# with pressing "right" button
def msRight(evt):
    # Text is shifted right by one position
    cnv.move(Txt,5,0)
# Width and height of the drawing area
W=600
H=400
# Width and height of the rectangle
w=200
h=100
# A number of lines
N=10
# Decrement for lengths of lines
d=20
# Radius of a circle
R=30
# Font
fnt=("Arial", 20, "bold")
# Text
txt="Blue text"
# Color of lines
clr="lightgreen"
# Color for the background of the drawing area
clr_1="lightyellow"
clr_2="yellow"
# Color to fill the circle
clr_C1="red"
clr_C2="white"
# Color to fill the rectangle
clr_R1="white"
clr_R2="green"
# Creating a window object
wnd=Tk()
# Window size and position
wnd.geometry(str(W+10)+"x"+str(H+10)+"+400+300")
# Window title
wnd.title("Graphics")
# Constant size window
wnd.resizable(False, False)
# Creating an drawing area object
cnv=Canvas(wnd, bg=clr_1, bd=3, relief=GROOVE)
# Placing the drawing area in the window
cnv.place(x=5, y=5, width=W, height=H)
# Transferring the focus of the drawing area
cnv.focus_set()
# Creating a text item
Txt=cnv.create_text(W/2,50, text=txt, font=fnt, fill="blue")
# Creating a group of horizontal lines
for k in range(N):
    # Coordinates of lines
    x1=70+k*d
    y1=H/4+10*k
    x2=W-70-d*k
    y2=H/4+10*k
    cnv.create_line(x1, y1, x2, y2, fill=clr, width=5, tag="Lns")
# Coordinates for creating a circle
x1=W/2-R
y1=H/2-R+30
x2=W/2+R
y2=H/2+R+30
# Creating a circle
Crl=cnv.create_oval(x1, y1, x2, y2, fill=clr_C1)
# Coordinates for creating a rectangle
x1=20
y1=H-h-20
x2=x1+w
y2=y1+h
# Creating a rectangle
Rtn=cnv.create_rectangle(x1, y1, x2, y2, fill=clr_R1)
# Creating image objects
img_1=PhotoImage(file="D:\\Programming\\Python\\Pictures\\smiles\\sad.png")
img_2=PhotoImage(file="D:\\Programming\\Python\\Pictures\\smiles\\smile.png")
# Creating an image object
Pct=cnv.create_image(W-20, H-20, anchor=SE, image=img_1)
# Registering handlers
cnv.bind("<Left>", msLeft)
cnv.bind("<Right>", msRight)
cnv.bind("<Up>",msUp)
cnv.bind("<Down>",msDown)
cnv.bind("<Enter>",msEnter)
cnv.bind("<Leave>",msLeave)
cnv.bind("<Motion>", msMotion)
cnv.bind("<Button-1>", lambda evt: cnv.config(bg=clr_2))
cnv.bind("<Button-3>", lambda evt: cnv.config(bg=clr_1))
# Displaying the main window
wnd.mainloop()