import tkinter
from tkinter import *

win = Tk()

l1 = Label(win, text="MATHS")
l1.place(x = 10, y = 10)

e1 = Entry(win, bd = 5)
e1.place(x = 60 , y = 10)

l2 = Label(win, text="English")
l2.place(x = 10, y = 60)

e2 = Entry(win, bd = 5)
e2.place(x = 60, y = 60)

b = Button(win, text = "submit")
b.place(x = 100, y = 100)

win.mainloop()
