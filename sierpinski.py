"""
sierpinski.py
plays the chaos game
11/15/16
"""
from __future__ import division
from visual import *
from visual.graph import *
from vis import *
from random import randint

# set up display and plotting
plot = gdisplay(x=0, y=400, height=400, width=400, title='Poincare Map', xtitle='y', ytitle='vy')
fun = gdots(color=color.blue)

# set up an equilateral triangle
a = vector(-50*sqrt(3), -50, 0)
b = vector(50*sqrt(3), -50, 0)
c = vector(0, 100, 0)
# square
# a = vector(-50, -50, 0)
# b = vector(50, -50, 0)
# c = vector(50, 50, 0)
# d = vector(-50, 50, 0)

oldpoint = sphere(pos=(0, 0, 0), radius=1, color=color.blue)

i = 0
while i < 10000:
    # Triangle
    r = randint(1, 3)
    if r == 1:
        newpoint = sphere(pos=(a + oldpoint.pos)/2, radius=1, color=color.red)
    elif r == 2:
        newpoint = sphere(pos=(b + oldpoint.pos)/2, radius=1, color=color.blue)
    elif r == 3:
        newpoint = sphere(pos=(c + oldpoint.pos)/2, radius=1, color=color.green)

    # Square
    # r = randint(1, 4)
    # if r == 1:
    #     newpoint = sphere(pos=(a + oldpoint.pos)/3, radius=1, color=color.red)
    # elif r == 2:
    #     newpoint = sphere(pos=(b + oldpoint.pos)/3, radius=1, color=color.blue)
    # elif r == 3:
    #     newpoint = sphere(pos=(c + oldpoint.pos)/3, radius=1, color=color.green)
    # elif r == 4:
    #     newpoint = sphere(pos=(d + oldpoint.pos)/3, radius=1, color=color.yellow)

    oldpoint = newpoint

    i += 1
