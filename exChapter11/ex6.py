from tkinter import *
from tkinter.ttk import Combobox
def change(evt):
    t=static_list.get()
    for k in range(len(names)):
        if t==names[k]:
            label.config(image=images[k])
            break
path="D:\\Programming\\Python\\Pictures\\girls\\"
names=["Ashen","Blonde","Brown","Brunette","Black", "Red"]
files=["ashen.png","blonde.png","brown-haired.png",
       "brunette.png","black.png","red.png"]
root=Tk()
root.title("Girls")
root.geometry("220x300")
images=[PhotoImage(file=path+f) for f in files]
index=0
label=Label(root, image=images[index])
label.pack(pady=20)
static_list=Combobox(root)
static_list.config(values=names)
static_list.current(index)
static_list.config(font=("Arial",11,"bold"))
static_list.bind("<<ComboboxSelected>>",change)
static_list.pack(pady=10)
btn=Button(root,text="Nice", width=7, height=2)
btn.config(command=root.destroy)
btn.pack(pady=10)
root.mainloop()