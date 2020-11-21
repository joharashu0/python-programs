import tkinter
from tkinter import *

win = Tk()

lb = Listbox(win)
lb.insert(1, "PYTHON")
lb.insert(2, "C")
lb.insert(3, "C++")
lb.insert(4, "C#")
lb.insert(5, "JAVA")
lb.pack()

win.mainloop()
