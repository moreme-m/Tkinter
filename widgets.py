from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.geometry("450x450")

#upload the image
uploaded = Image.open("download (1).webp")

#process the image for tkinter

fish = ImageTk.PhotoImage(uploaded)

goldfish = Label(window, image=fish, width=300, height=300)
goldfish.pack()

def msg():
    messagebox.showerror("Error", "An error occured!")
    messagebox.showinfo("Information", "You just won 1m dollars")
    messagebox.showwarning("Alert", "VIRUS DETECTED!")
    messagebox.askquestion("Question", "Do you like pizza?")
    messagebox.askretrycancel("qsn", "Loading error!")
    messagebox.askyesnocancel("qsn", "Do you like coding?")

btn = Button(window, text="click here!", bg="gold", command=msg)
btn.pack()

window.mainloop()