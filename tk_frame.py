import tkinter
from tkinter import *

win = Tk()

frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side = BOTTOM)

rb = Button(frame, text="Red", fg='red')
rb.pack(side = LEFT)

win.mainloop()
