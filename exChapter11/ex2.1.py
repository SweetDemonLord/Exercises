from tkinter import *
def msMotion(evt):
    x=evt.x
    y=evt.y
    Rxy=[100,67,300,253]
    if Rxy[0] < x < Rxy[2] and Rxy[1] < y < Rxy[3]:
        cnv.itemconfig(Pct, image=imgs[1])
    else:
        cnv.itemconfig(Pct, image=imgs[0])
wnd=Tk()
wnd.title("Упражнение 2 главы 11")
wnd.geometry("500x400")
wnd.resizable(False,False)
path="D:\\Programming\\Python\\Pictures\\вк\\"
files=["опа.png","vk.png"]
imgs=[PhotoImage(file=path+f) for f in files]
index=0
cnv=Canvas(wnd,width=400,height=300)
cnv.place(x=50,y=10, width=400, height=300)
cnv.focus_set()
Pct=cnv.create_image(200,150,image=imgs[index])
cnv.bind("<Motion>",msMotion)
#cnv.bind("<Motion>",msMotion)
btn=Button(wnd,text="Закрыть",command=wnd.destroy)
btn.place(x=220,y=320,width=60,height=30)
wnd.mainloop()