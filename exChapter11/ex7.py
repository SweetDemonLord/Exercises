from tkinter import *
def choose_color(*args):
    window.config(background=color.get())
    if color.get() == "Black":
        label.config(foreground="White")
        for r in radiobuttons:
            r.config(foreground="White")
    else:
        label.config(foreground="Black")
        for r in radiobuttons:
            r.config(foreground="Black")
    label.config(background=color.get())
    for r in radiobuttons:
        r.config(background=color.get())
W=600
H=500
window = Tk()
window.title("Exercise №7 of the 11th chapter")
colors=["White","Pink","Purple","Red","Yellow","Turquoise",
        "Orange","Blue","Green","Violet","Brown","Black"]
window.geometry(str(W) + "x" + str(H))
label=Label(window, text="Choose your favourite color", background="White",
            font=("Arial", 16, "bold", "italic"))
label.pack(padx=5, pady=5)
color=StringVar()
radiobuttons=[Radiobutton(window, text=c, background="White",
                          font=("Arial",10,"italic"),variable=color, value=c) for c in colors]
for radiobutton in radiobuttons:
    radiobutton.pack(side="top",padx=5, pady=5)
color.set("White")
choose_color()
color.trace("w",choose_color)
window.mainloop()