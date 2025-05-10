from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.title("Denomination Calculator")
window.config(bg="aqua")
window.geometry("500x500")

uploaded = Image.open("cash tally.jpeg")
cash = ImageTk.PhotoImage(uploaded)

label1 = Label(window, image= cash)
label1.pack()

label2 = Label(window, text="Welcome to the denomination calculator", bg="aqua")
label2.pack()

def msg():
    message = messagebox.showinfo("Message", "Are you sure you wwant to proceed?")
    if message == "ok":
        topwin()

btn = Button(window, text="Let's get started!", bg="yellow", command = msg)
btn.pack()


def topwin():
    top = Toplevel()
    top.geometry("450x450")
    top.configure(bg ="pink")
    top.title("Denomination counter")

    l1 = Label(top, text="Enter the amount")
    entry1 = Entry(top)
    l1.place(x=150, y=50)
    entry1.place(x=135, y=80)









window.mainloop()