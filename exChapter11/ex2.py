from tkinter import *
def msEnter(evt):
    cnv.itemconfig(Pct, image=imgs[1])
def msLeave(evt):
    cnv.itemconfig(Pct, image=imgs[0])
wnd=Tk()
wnd.title("Упражнение 2 главы 11")
wnd.geometry("500x400")
wnd.resizable(False,False)
path="D:\\Programming\\Python\\Pictures\\вк\\"
files=["опа.png","vk.png"]
imgs=[PhotoImage(file=path+f) for f in files]
index=0
cnv=Canvas(wnd,width=300,height=186)
cnv.place(x=100,y=88, width=300, height=176)
cnv.focus_set()
Pct=cnv.create_image(150,88,image=imgs[index])
cnv.bind("<Enter>",msEnter)
cnv.bind("<Leave>",msLeave)
#cnv.bind("<Motion>",msMotion)
btn=Button(wnd,text="Закрыть",command=wnd.destroy)
btn.place(x=220,y=280,width=60,height=30)
wnd.mainloop()