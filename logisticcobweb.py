"""
logisticcobweb.py
iterates of 4rx(1-x) graphical solution
"""
from visual import *
from visual.controls import *
from vis import *

r = 0.26
i = 0
scene = display(x=200, y=0, height=600, width=1000, userzoom=0, userspin=0, background=color.white, center=(250, 150),
                range=(270, 300, 10), title='x=4rx(1-x)')
graph = curve(color=color.yellow)
iterate_plot = curve(color=color.red)

# makes axes in main window
curve(color=color.black, pos=[(0, -5), (0, 300)])
curve(color=color.black, pos=[(-5, 0), (500, 0)])
curve(color=color.blue, pos=[(0, 0), (400, 300)])
for j in arange(10, 501, 10):
    curve(color=color.black, pos=[(j, -5), (j, 5)])
for j in arange(10, 301, 10):
    curve(color=color.black, pos=[(-5, j), (5, j)])
label(pos=(0, 310), text='y', box=0, line=0, color=color.black, opacity=0)
label(pos=(510, 0), text='x', box=0, line=0, color=color.black, opacity=0)
label(pos=(150, 305), text='Graphical method to find attractors', box=0, line=0, color=color.black, opacity=0)


def adjust(object, val):
    object.value += val
    set()


c = controls(x=0, y=0, width=200, height=600, background=color.white)

rslider = slider(pos=(-10, -80), width=7, length=160, axis=(0, 1, 0), min=0, max=1, action=lambda: set())
r_minus_button = button(pos=(-10, -81.5), height=3, width=3, text='-', action=lambda: adjust(rslider, -.01))
r_plus_button = button(pos=(-10, 81.5), height=3, width=3, text='+', action=lambda: adjust(rslider, .01))
r_text = label(pos=(-10, -90), text='r = %i' % (100 * r), display=c.display, box=0, line=0, color=color.black,
               opacity=0)
rslider.value = r
islider = slider(pos=(10, -80), width=7, length=160, axis=(0, 1, 0), min=0, max=5, action=lambda: set())
i_minus_button = button(pos=(10, -81.5), height=3, width=3, text='-', action=lambda: adjust(islider, -1))
i_plus_button = button(pos=(10, 81.5), height=3, width=3, text='+', action=lambda: adjust(islider, 1))
i_text = label(pos=(10, -90), text='i = %i' % (i + 1), display=c.display, box=0, line=0, color=color.black, opacity=0)
islider.value = i


def set():
    global r, i
    i = islider.value
    r = rslider.value
    r_text.text = 'r = %i' % (100 * r)
    i_text.text = 'i = %i' % (i + 1)
    go()


def iterate(X, j):
    global r
    iter2 = j
    if (iter2 > 1):
        iter2 = iter2 - 1
        yy = iterate(X, iter2)
        z = 4 * r * yy * (1 - yy)
    else:
        z = 4 * r * X * (1 - X)
    return z


def go():
    global graph, iterate_plot, r, i
    x = 0.4
    graph.pos = []
    iterate_plot.pos = []
    n = 200
    delta = 1. / n
    y = 0
    xx = 0
    for j in arange(2, n + 1, 1):
        xx = xx + delta
        y = iterate(xx, i)
        graph.append(pos=(400 * xx, 300 * y))
    y0 = 0.
    x0 = x
    n = 100
    for j in arange(2, n + 1, 1):
        y = iterate(x, i)
        iterate_plot.append(pos=(x0 * 400, y0 * 300))
        iterate_plot.append(pos=(x0 * 400, y * 300))
        iterate_plot.append(pos=((400 * y), y * 300))
        x0 = y
        y0 = y
        x = y


while 1:
    c.interact()
