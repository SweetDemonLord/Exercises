from tkinter import *
# Function for font characterization
def getFont():
    # An empty list
    res=[]
    # Font name
    name=lst.get(lst.curselection())
    # Font size
    size=scl.get()
    # Adding an item to the list
    res.append(name)
    res.append(size)
    # If the option to apply
    # bold style is set
    if bold.get()!="":
        res.append(bold.get())
    # If the option to apply
    # italic style is set
    if italic.get()!="":
        res.append(italic.get())
    # Function result
    return res
# Function for applying font parameters
def setAll(*args):
    # Font calculation
    fnt=getFont()
    # Applying font to text in the window
    lbl.configure(font=fnt)
    # Defining color for text in the window
    lbl.configure(fg=color.get())
    # Defining a template text
    # to be displayed in the window
    txt="\nFont "
    # Font name
    txt+=fnt[0]
    # Font size
    txt+=" size "+str(fnt[1])+"\n"
    # If bold style is applied
    if "bold" in fnt:
        txt+=" bold"
    # If italic style is applied
    if "italic" in fnt:
        txt+=" italic"
    # Font color
    if color.get()=="red":
        txt+=" red"
    elif color.get()=="blue":
        txt+=" blue"
    else:
        txt+=" black"
    txt+=" color\n"
    # Displaying text in the window
    text.set(txt)
# Lists font characteristics
fnt_1=["Arial",12,"italic"]
fnt_2=["Times New Roman",13,"bold","italic"]
# List with font names for a static list
fonts=["Times New Roman", "Arial", "Courier New"]
# Minimum font size
min_size=15
# Maximum font size
max_size=21
# Window width and height
W=640
H=420
# Height of the frame with template text
Hf=140
# Width and height of the frame with a static list
Wl=W/3
Hl=H-Hf-15
# Height of the frame with a button
Hb=60
# Width and height of the frame with a slider and radio button
Ws=W-Wl-15
Hs=Hl-Hb-5
# Window creation
wnd=Tk()
wnd.title("Font parameters")
wnd.geometry(str(W)+"x"+str(H))
wnd.resizable(False,False)
# Frames creation
frm_scale=Frame(wnd,bd=3,relief=GROOVE)
frm_text=Frame(wnd,bd=3,relief=GROOVE)
frm_btn=Frame(wnd,bd=3,relief=GROOVE)
frm_list=Frame(wnd,bd=3,relief=GROOVE)
frm_check=Frame(frm_list,bd=3,relief=GROOVE)
# Variables for defining text
# content in controls
text=StringVar()
color=StringVar()
bold=StringVar()
italic=StringVar()
# Creating text labels
lbl_text=Label(frm_text, text="Example text:",font=fnt_2)
lbl_color=Label(frm_scale, text="Text color:",font=fnt_2)
lbl_size=Label(frm_scale, text="Font size:",font=fnt_2)
lbl_font=Label(frm_list,text="Font name:",font=fnt_2)
lbl_style=Label(frm_check, text="Font style:",font=fnt_2)
# Label for displaying a template text
lbl=Label(frm_text, textvariable=text)
# Background and frame for the label
lbl.configure(bg="white",relief=RAISED)
# Radio buttons
rb_1=Radiobutton(frm_scale, text="red",variable=color)
rb_1.configure(value="red",font=fnt_1)
rb_2=Radiobutton(frm_scale, text="blue",variable=color)
rb_2.configure(value="blue",font=fnt_1)
rb_3=Radiobutton(frm_scale, text="black",variable=color)
rb_3.configure(value="black",font=fnt_1)
# Set by radio button
color.set("blue")
# Slider creation
scl=Scale(frm_scale, orient=HORIZONTAL)
# Value change range
scl.configure(from_=min_size,to=max_size)
# Interval for caption display and sampling step
# for slider position
scl.configure(tickinterval=1, resolution=1)
# Handler for event related
# to changing the slider position
scl.configure(command=setAll)
# Creating options and customizing their parameters
chb_1=Checkbutton(frm_check, text="bold",variable=bold)
chb_1.configure(onvalue="bold",offvalue="",font=fnt_1)
chb_2=Checkbutton(frm_check, text="italic",variable=italic)
chb_2.configure(onvalue="italic",offvalue="",font=fnt_1)
# Initial state of an option
bold.set("")
italic.set("italic")
# Static list creation
lst=Listbox(frm_list,selectmode=SINGLE, font=fnt_1)
# Background color and highlighting an item
lst.configure(bg="gray96",selectbackground="gray")
# The way to highlight the item and the height of the list
lst.configure(activestyle="none", height=len(fonts)+1)
# Filling the static list by items
for n in fonts:
    lst.insert(END,n)
# By default, the first item is selected
lst.select_set(0)
# Handler for a static list
lst.bind("<<ListboxSelect>>",setAll)
# Button creation
btn=Button(frm_btn,text="OK",font=fnt_2)
# Handler for the button
btn.configure(command=wnd.destroy)
# Placement of labels and the slider on the frames
lbl_text.pack(side="top",fill="x",padx=5,pady=5)
lbl.pack(side="top",fill="both",padx=5,pady=5)
lbl_color.pack(side="top",fill="x",padx=5,pady=5)
scl.pack(side="bottom",fill="x",padx=5,pady=5)
lbl_size.pack(side="bottom",fill="x",padx=5,pady=(25,5))
lbl_font.pack(side="top",fill="x",padx=5,pady=5)
lbl_style.pack(side="top",fill="x",padx=5,pady=5)
# Radio buttons placement
rb_1.pack(side="left",fill="x",padx=5,pady=5)
rb_2.pack(side="left",fill="x",padx=5,pady=5)
rb_3.pack(side="left",fill="x",padx=5,pady=5)
# Placement of options
chb_1.pack(side="left",fill="x",padx=5,pady=5)
chb_2.pack(side="left",fill="x",padx=5,pady=5)
# Placement of a static list
lst.pack(side="top",fill="x",padx=5,pady=5)
# Placement of the button
btn.pack(side="bottom",fill="x",padx=5,pady=10)
# Placement of the frames
frm_text.place(x=5, y=5, width=W-10, height=Hf)
frm_check.pack(side="bottom", fill="both", padx=5, pady=5)
frm_list.place(x=5, y=Hf+10, height=Hl, width=Wl)
frm_scale.place(x=Wl+10, y=Hf+10, width=Ws, height=Hs)
frm_btn.place(x=Wl+10, y=Hf+Hs+15, width=Ws, height=Hb)
# Applying font settings to template text
setAll()
# Variable value tracking mode
color.trace("w",setAll)
bold.trace("w",setAll)
italic.trace("w",setAll)
# Displaying the window
wnd.mainloop()