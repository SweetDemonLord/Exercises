from tkinter import *
def setMenuImageAshen(*args):
       label.config(image=images[0])
def setMenuImageBlonde(*args):
       label.config(image=images[1])
def setMenuImageBrown(*args):
       label.config(image=images[2])
def setMenuImageBrunette(*args):
       label.config(image=images[3])
def setMenuImageBlack(*args):
       label.config(image=images[4])
def setMenuImageRed(*args):
       label.config(image=images[5])
W=500
H=400
path="D:\\Programming\\Python\\Pictures\\girls\\"
files=["ashen.png","blonde.png","brown-haired.png",
       "brunette.png","black.png","red.png"]
window = Tk()
window.title("Exercise №8 of the 11th chapter")
window.geometry(str(W) + "x" + str(H))
images=[PhotoImage(file=path+f) for f in files]
menubar = Menu(window)
mAshen = Menu(menubar, font="Arial", tearoff=0)
mBlonde = Menu(menubar, font="Arial", tearoff=0)
mBrown = Menu(menubar, font="Arial", tearoff=0)
mBrunette = Menu(menubar, font="Arial", tearoff=0)
mBlack = Menu(menubar, font="Arial", tearoff=0)
mRed = Menu(menubar, font="Arial", tearoff=0)
menubar.add_radiobutton(label="Ashen", command=setMenuImageAshen)
menubar.add_radiobutton(label="Blonde", command=setMenuImageBlonde)
menubar.add_radiobutton(label="Brown", command=setMenuImageBrown)
menubar.add_radiobutton(label="Brunette", command=setMenuImageBrunette)
menubar.add_radiobutton(label="Black", command=setMenuImageBlack)
menubar.add_radiobutton(label="Red", command=setMenuImageRed)
window.config(menu=menubar)
label=Label(window, image=images[1])
label.pack(side=TOP, pady=100)
window.mainloop()