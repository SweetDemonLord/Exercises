from tkinter import *
wnd=Tk()
wnd.title("Exercise №1 of the 11th chapter")
wnd.geometry("700x500")
wnd.resizable(False,False)
lbl=Label(wnd, text="Я живу по Омар Хайяму", font=("Calibri Italic", 20))
lbl.place(x=200, y=60)
path="D:\\Programming\\Python\\Pictures\\2OmarKhayyam.png"
img=PhotoImage(file=path)
lbl=Label(wnd, image=img)
lbl.place(x=125, y=100, width=450, height=300)
btn=Button(wnd,text="Based", font=("Calibri Italic", 14), command=wnd.destroy)
btn.place(x=330, y=360, width=60, height=30)
wnd.mainloop()
