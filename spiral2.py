import turtle as t
import time as te
from itertools import cycle

colors = cycle(['red','blue','green','orange','white','purple','grey','pink','yellow'])

def circle(size,angle,shift,shape):
    t.pencolor(next(colors))
    next_shape = ''
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size*2)
            t.left(90)
        next_shape = 'circle'
    t.right(angle)
    t.forward(shift)
    circle(size+5,angle+1,shift+1,next_shape)


t.bgcolor('black')
t.speed('slow')
t.pensize(3)

circle(30,0,1,'circle')

te.sleep(5)
t.hideturtle()
