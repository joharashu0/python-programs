import tkinter
from tkinter import *
from functools import partial

win = Tk()

def sum(label, x1, x2):
    x1 = (x1.get())
    x2 = (x2.get())
    sum = int(x1) + int(x2)
    label.config(text='sum is :%d' %sum)
    return

l1 = Label(win, text="first num")
l1.grid(row = 1, column = 0)
l2 = Label(win, text="second num")
l2.grid(row = 2, column = 0)
label = Label(win)
label.grid(row = 6, column = 0)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win, textvariable = x1)
e1.grid(row = 1, column = 2)
e2 = Entry(win, textvariable = x2)
e2.grid(row = 2, column = 2)

sum = partial(sum, label, x1, x2)

button = Button(win, text = 'calculate', command = sum)
button.grid(row = 3, column = 0)

win.mainloop()
