#window or root can be used. Or any other name
#widget is what you add in the tkinter
from tkinter import *

window = Tk()
window.geometry("450x450")
window.configure(bg="beige")
window.title("My first APP")

#widget
welcome = Label(window, text="Welcome!!", bg="pink", fg="red", font=("garamond",20))
welcome.pack()

btn = Button(window, text="click Here!", bg="gold")
btn.pack()

entry = Entry(window, bg="orange")
entry.pack()

text = Text(window)
text.pack()

window.mainloop()