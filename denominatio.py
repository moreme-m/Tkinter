from tkinter import *
from PIL import Image, ImageTk

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

btn = Button(window, text="Let's get started!", bg="blue")
btn.pack()







window.mainloop()