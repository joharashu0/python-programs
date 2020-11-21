import tkinter
from tkinter import *

win Tk()

def nothing():
    file = Toplevel(win)
    button = Button(file, text='do not')
    button.pack()

menubar = Menu(win)
filemenu.add_command(label="New window", command = nothing)
filemenu.add_separator()
manubar.add_cascade(label, = "file", menu = filemenu)

win.config(menu=menubar)
win.mainloop()
