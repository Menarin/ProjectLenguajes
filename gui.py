from tkinter import *
from tkinter import scrolledtext


window = Tk()

window.title("Python expression checker")

lbl = Label(window, text="Your expression: ")

lbl.grid(column=0, row=0)

txt = Entry(window, width=10)

txt.grid(column=1, row=0)

txt2 = scrolledtext.ScrolledText(window, width=30, height=10)

txt2.grid(column=0, row=2, sticky=W)


def clicked():
    text = txt.get()
    res = "Your expression:  " + text
    lbl.configure(text=res)
    return text


btn = Button(window, text="Check", command=clicked)

btn.grid(column=2, row=0)

# window.mainloop()
