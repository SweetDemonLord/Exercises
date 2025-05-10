from tkinter import *
from tkinter.messagebox import *
# Class for creating a window
class MyApp:
    # Constructor
    def __init__(self):
        # Customizing parameters
        self.setValues()
        # Creating the main window
        self.makeMainWindow()
        # Defining "variables" for event handling
        self.setVars()
        # Creating the main menu
        self.makeMainMenu()
        # Creating a toolbar
        self.makeToolBar()
        # Creating an auxiliary panel
        self.makeFrame()
        # Creating a context menu
        self.makePopupMenu()
        # Calculating parameters of template text
        self.apply()
        # Tracking "variables" mode
        self.traceVars()
        # Displaying the main window
        self.showMainWindow()
    # Method for setting parameters
    def setValues(self):
        # Window width and height
        self.W=500
        self.H=200
        # Toolbar height
        self.h=40
        # Size of the main window
        self.position=str(self.W)+'x'+str(self.H)
        # Font names
        self.fonts=["Times New Roman","Arial","Courier New"]
        # Dictionary with color names
        self.colors={"red":"Red","blue":"Blue","black":"Black"}
        # List with style names
        self.style=[["bold","Bold"],["italic","Italic"]]
        # List with file names with images
        self.imgFiles=["exit.png","bold.png","italic.png","normal.png"]
        # File directory path
        self.path="D:\\Programming\\Python\\Pictures\\icons\\"
        # Main font
        self.font=("Courier New",10,"bold")
    # Method for creating the main window
    def makeMainWindow(self):
        self.wnd=Tk()
        self.wnd.title("Define a font")
        self.wnd.geometry(self.position)
        self.wnd.resizable(False,False)
    # Method for displaying the main window
    def showMainWindow(self):
        self.wnd.mainloop()
    # Method for creating the main menu
    def makeMainMenu(self):
        # Creating an object for the toolbar
        self.menubar=Menu(self.wnd)
        # Creating items of the main menu
        self.mFont=Menu(self.wnd, font=self.font, tearoff=0)
        self.mStyle=Menu(self.wnd, font=self.font, tearoff=0)
        self.mColor=Menu(self.wnd, font=self.font, tearoff=0)
        self.mAbout=Menu(self.wnd, font=self.font, tearoff=0)
        # Filling menu times
        self.setMenuFont(self.mFont)
        self.setMenuStyle(self.mStyle)
        self.setMenuColor(self.mColor)
        # Filling the last menu item
        self.mAbout.add_command(label="About program", command=self.showDialog)
        # Adding a separator
        self.mAbout.add_separator()
        self.mAbout.add_command(label="Exit", command=self.clExit)
        # Adding menu items to the menu bar
        self.menubar.add_cascade(label="Font", menu=self.mFont)
        self.menubar.add_cascade(label="Style",menu=self.mStyle)
        self.menubar.add_cascade(label="Color", menu=self.mColor)
        self.menubar.add_cascade(label="Program", menu=self.mAbout)
        # Setting the main menu for the window
        self.wnd.config(menu=self.menubar)
    # Method for creating a toolbar
    def makeToolBar(self):
        # List with method names for handling
        # the event related to button presses
        mt=[self.clExit, self.clBold, self.clItalic, self.clNormal]
        # Frame for placing buttons
        self.toolbar=Frame(self.wnd, bd=3, relief=GROOVE)
        # List for images
        self.imgs=[]
        # List for buttons
        self.btns=[]
        # Creating images and buttons
        for f in self.imgFiles:
            # Creating an image
            self.imgs.append(PhotoImage(file=self.path+f))
            # Creating a button
            self.btns.append(Button(self.toolbar, image=self.imgs[-1]))
            # Adding the button on the frame
            self.btns[-1].pack(side="left",padx=2,pady=2)
        # Defining handlers for buttons
        for k in range(len(mt)):
            self.btns[k].configure(command=mt[k])
        # Creating a text label
        self.lblSize=Label(self.toolbar, text="Font size:", font=self.font)
        # Placing the label on the frame
        self.lblSize.pack(side="left", padx=2, pady=2)
        # Creating a spinner
        self.spnSize=Spinbox(self.toolbar, from_=15, to=20, font=self.font,
                             width=3, justify="right", textvariable=self.size)
        # Placing the spinner on the frame
        self.spnSize.pack(side="left", padx=2, pady=2)
        # Placing the frame in the window
        self.toolbar.place(x=3, y=3, width=self.W-6, height=self.h)
    # Method for creating an auxiliary frame
    def makeFrame(self):
        # Creating an auxiliary frame
        self.frame=Frame(self.wnd, bd=3, relief=GROOVE)
        # Creating a label and adding its on the frame
        Label(self.frame, text="Example text:", font=self.font).pack(side="top")
        # Creating a label for displaying
        # template text
        self.lblText=Label(self.frame, textvariable=self.text, relief=GROOVE,
                            bg="white", height=5)
        # Placing the label on the auxiliary frame
        self.lblText.pack(side="top", fill="both", padx=1, pady=1)
        # Placing the auxiliary frame in the window
        self.frame.place(x=3, y=self.h+9, width=self.W-6, height=self.H-self.h-12)
    # Method for creating a context menu
    def makePopupMenu(self):
        # Creating a context menu object
        self.popup=Menu(self.wnd, tearoff=0, font=self.font)
        # Adding commands to the context menu
        self.setMenuFont(self.popup)
        # Adding a separator
        self.popup.add_separator()
        # Adding commands to the context menu
        self.setMenuStyle(self.popup)
        # Adding a separator
        self.popup.add_separator()
        # Adding commands to the context menu
        self.setMenuColor(self.popup)
        # Adding a separator
        self.popup.add_separator()
        # Adding a command to the context menu
        self.popup.add_command(label="Exit", command=self.clExit)
        # Defining an event handler
        # for the context menu
        self.wnd.bind("<Button-3>", lambda evt: self.popup.tk_popup(evt.x_root,
                        evt.y_root))
    # Method for forming menu commands
    # related to font selection
    def setMenuFont(self, menu):
        for f in self.fonts:
            menu.add_radiobutton(label=f, value=f, variable=self.name)
        self.name.set(self.fonts[0])
    # Method for forming menu commands
    # related to style selection
    def setMenuStyle(self, menu):
        for k in range(len(self.style)):
            menu.add_checkbutton(label=self.style[k][1], onvalue=True,
                                 offvalue=False, variable=self.bi[k])
            self.bi[0].set(True)
            self.bi[1].set(False)
    # Method for forming menu commands
    # related to color selection
    def setMenuColor(self, menu):
        for r in self.colors.keys():
            menu.add_radiobutton(label=self.colors[r], value=r,
                variable=self.color)
        self.color.set("blue")
    # Method for defining font parameters and
    # calculating template text
    def apply(self,*args):
        # Color for font
        clr=self.color.get()
        # Font name
        nm=self.name.get()
        # Font size
        sz=self.size.get()
        # Applying color to a label
        self.lblText.configure(fg=clr)
        # List with font parameters
        fnt=[nm, sz]
        # Formation of template text and
        # definition of font parameters
        txt=self.colors[clr]+" font "+nm+"\n"
        for k in range(len(self.style)):
            if self.bi[k].get():
                fnt.append(self.style[k][0])
                txt+=self.style[k][1].lower()+" "
        txt+="size "+str(sz)
        # Applying a font to the label
        self.lblText.configure(font=fnt)
        # Setting text for the label
        self.text.set(txt)
    # Method for creating "variables" used
    # for event handling
    def setVars(self):
        self.text=StringVar()
        self.name=StringVar()
        self.bi=[BooleanVar(), BooleanVar()]
        self.size=IntVar()
        self.color=StringVar()
    # Method for switching to the tracking mode
    # of "variables" values
    def traceVars(self):
        mt=self.apply
        self.name.trace("w", mt)
        self.color.trace("w", mt)
        for k in range(len(self.bi)):
            self.bi[k].trace("w", mt)
        self.size.trace("w", mt)
    # Method for handling a button press
    # to terminate work
    def clExit(self):
        self.wnd.destroy()
    # Method to handle pressing the button
    # to apply/cancel bold style
    def clBold(self):
        self.bi[0].set(not self.bi[0].get())
    # Method to handle pressing the button
    # to apply/cancel italic style
    def clItalic(self):
        self.bi[1].set(not self.bi[1].get())
    # Method to handle pressing the button
    # to cancel bold and italic style
    def clNormal(self):
        self.bi[0].set(False)
        self.bi[1].set(False)
    # Method for displaying the window with a message
    def showDialog(self):
        showinfo("About program", "Very simple program")
    # Displaying the window on the screen
MyApp()