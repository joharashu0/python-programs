import turtle as t
import time as te
from itertools import cycle

colors = cycle(['red','blue','green','orange','white','purple','grey','pink','yellow'])

def circle(size,angle,shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    circle(size+5,angle+1,shift+1)


t.bgcolor('black')
t.speed('slow')
t.pensize(3)

circle(30,0,1)

te.sleep(5)
t.hideturtle()
