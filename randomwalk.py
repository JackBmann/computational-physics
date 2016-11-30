"""
randomwalk.py
11/18/16
"""
from __future__ import division
from visual import *
from vis import *
from random import random
from visual.graph import *

# set up scene
scene = display(x=300, y=0, width=800, height=800)
no_walkers = 200
walker_radius = 1.0

# define step length
step = 1

avg_distance = 0
distance_squared = 0
t = 0

# set up graphs
graph1 = gdisplay(x=0, y=0, width=300, height=200, title='Average Distance vs. Time')
graph2 = gdisplay(x=0, y=200, width=300, height=200, title='Theoretical Distance vs. Time')
graph3 = gdisplay(x=0, y=400, width=300, height=200, title='Diffusion vs. Time')

plot1 = gcurve(gdisplay=graph1, color=color.white)
plot2 = gcurve(gdisplay=graph2, color=color.yellow)
plot3 = gcurve(gdisplay=graph3, color=color.blue)

# create walkers
walker_list = []
for i in range(no_walkers):
    hue = (random(), random(), random())
    walker = sphere(radius=walker_radius, color=hue)
    walker.pos = vector(0, 0, 0)
    walker_list.append(walker)
    walker_list[i].trail = curve(pos=walker_list[i].pos, color=hue, radius=0.1)


# move those walkers
def move():
    for i in range(no_walkers):
        r = random()
        # Normal
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
        # With gravity
        # if r <= 1/7:
        #     walker_list[i].pos.x += step
        # elif r <= 2/7:
        #     walker_list[i].pos.x -= step
        # elif r <= 3/7:
        #     walker_list[i].pos.y += step
        # elif r <= 5/7:
        #     walker_list[i].pos.y -= step
        # elif r <= 6/7:
        #     walker_list[i].pos.z += step
        # else:
        #     walker_list[i].pos.z -= step
        walker_list[i].trail.append(pos=walker_list[i].pos)

while True:
    for i in range(no_walkers):
        avg_distance += mag(walker_list[i].pos)
        distance_squared += mag(walker_list[i].pos)**2

    avg_distance /= no_walkers
    distance_squared /= no_walkers
    t += 1  # increment Monte Carlo time by one unit

    diffusion = (distance_squared - avg_distance**2) / (4*t)
    plot1.plot(pos=(t, avg_distance))
    plot2.plot(pos=(t, sqrt(t)))
    plot3.plot(pos=(t, diffusion))

    move()
    rate(300)
