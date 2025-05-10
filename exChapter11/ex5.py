from tkinter import *
def increase_clicked():
    global t
    if t < 25:
        t = t + 1
        lbl.config(font=("Arial", t,"bold","italic"))
def decrease_clicked():
    global t
    if t > 1:
        t = t - 1
        lbl.config(font=("Arial", t,"bold","italic"))
wnd=Tk()
wnd.title("Exercise №5 of the 11th chapter")
wnd.geometry("500x300")
t=13
fnt=("Arial",t,"bold","italic")
lbl=Label(master=wnd, text="Welcome to the new world!", font=fnt)
lbl.pack(pady=70)
btn1=Button(master=wnd, text="Increase", font=fnt)
btn1.pack(pady=10)
btn1.config(command=increase_clicked)
btn2=Button(master=wnd, text="Decrease", font=fnt)
btn2.pack(pady=10)
btn2.config(command=decrease_clicked)
wnd.mainloop()