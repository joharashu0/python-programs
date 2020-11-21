import tkinter
from tkinter import *

win = Tk()

c1 = IntVar()
c2 = IntVar()

cb = Checkbutton(win, text="Music", offvalue=0, onvalue=1, height=5, width=10, variable=c1)
cb.pack()
cb2 = Checkbutton(win, text="Audio", offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb2.pack()

var = IntVar()

r1 =Radiobutton(win, text="option1", variable=var, value=1)
r1.pack()
r2 =Radiobutton(win, text="option2", variable=var, value=2)
r2.pack()

win.mainloop()
