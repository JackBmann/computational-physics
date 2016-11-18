"""
randomwalk.py
11/18/16
"""
from __future__ import division
from visual import *
from vis import *
from random import random

# set up scene
scene = display(x=300, y=0, width=800, height=800)
no_walkers = 200
walker_radius = 1.0

# define step length
step = 1

# create walkers
walker_list = []
for i in range(no_walkers):
    hue = (random(), random(), random())
    walker = sphere(radius=walker_radius, color=hue)
    walker.pos = vector(0, 0, 0)
    walker_list.append(walker)


# move those walkers
def move():
    for i in range(no_walkers):
        r = random()
        if r <= 1/6:
            walker_list[i].pos.x += step
        elif r <= 1/3:
            walker_list[i].pos.x -= step
        elif r <= 1/2:
            walker_list[i].pos.y += step
        elif r <= 2/3:
            walker_list[i].pos.y -= step
        elif r <= 5/6:
            walker_list[i].pos.z += step
        else:
            walker_list[i].pos.z -= step

while True:
    move()
    rate(300)
