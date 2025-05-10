from tkinter import *
def msUp(evt):
    canvas.move(circle,-5,-5)
def msDown(evt):
    canvas.move(circle,5,5)
def msLeft(evt):
    canvas.move(circle,-5,5)
def msRight(evt):
    canvas.move(circle,5,-5)
W=600
H=400
window=Tk()
window.title("Exercise №10 of the 11th chapter")
window.geometry(str(W)+"x"+str(H))
window.resizable(False,False)
canvas=Canvas(window,width=W,height=H)
canvas.pack()
canvas.focus_set()
R=50
x1=W/2-R
y1=H/2-R
x2=W/2+R
y2=H/2+R
circle=canvas.create_oval(x1,y1,x2,y2,fill='black')
canvas.bind('<Up>',msUp)
canvas.bind('<Down>',msDown)
canvas.bind('<Left>',msLeft)
canvas.bind('<Right>',msRight)
window.mainloop()