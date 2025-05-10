from tkinter import *
from tkinter import messagebox


def enter_expression(*args):
    lbl.config(text="Everything is awesome!",
                font=("Arial", 10, "italic"), bg="white")
    try:
        expression = eval(entry.get())
        label.config(text="=" + str(expression))
    except (NameError,TypeError):
        messagebox.showerror(title="Error", message="Please enter a valid expression.")
    except SyntaxError:
        lbl.config(bg="red",text="Don't forget enter only arithmetic operations and numbers.")


window = Tk()
window.geometry("400x300")
window.title("Exercise №9 of the 11th chapter")
label=Label(window,text="Enter an algebraic expression:",
            font=("Arial", 15, "italic"))
label.pack(padx=10,pady=20)
entry=Entry(window, font=("Arial", 15))
entry.pack(padx=10,pady=40)
label=Label(window,text="=", font=("Arial", 15))
label.pack(padx=10,pady=10)
lbl = Label(window)
lbl.pack(padx=5, pady=5)
entry.bind("<KeyRelease>", enter_expression)
window.mainloop()