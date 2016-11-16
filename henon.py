"""
henon.py
create Poincare map for the Henon-Heiles potential
11/15/16
"""
from __future__ import division
from visual.graph import *

# set up display and plotting
plot = gdisplay(x=0, y=400, height=400, width=400, title='Poincare Map', xtitle='y', ytitle='vy')
fun = gdots(color=color.blue)

# set initial values
t = 0
h = 0.01
x = 0.5
vx = 0
y = 0
vy = 0.225


def ax(x, y):
    return -x - 2*x*y


def ay(x, y):
    return -y - x**2 + y**2


E = 0.5*(vx**2 + vy**2) + 0.5*(x**2 + y**2) + x**2*y - y**3/3
print "E = ", E

# implement Runge-Kutta
while t < 5000:
    k1vx = ax(x, y)*h
    k1x = vx*h

    k1vy = ay(x, y)*h
    k1y = vy*h

    k2vx = ax(x + k1x/2, y + k1y/2)*h
    k2x = (vx + k1vx/2)*h

    k2vy = ay(x + k1x/2, y + k1y/2)*h
    k2y = (vy + k1vy/2)*h

    k3vx = ax(x + k2x/2, y + k2y/2)*h
    k3x = (vx + k2vx/2)*h

    k3vy = ay(x + k2x/2, y + k2y/2)*h
    k3y = (vy + k2vy/2)*h

    k4vx = ax(x + k3x, y + k3y)*h
    k4x = (vx + k3vx)*h

    k4vy = ay(x + k3x, y + k3y)*h
    k4y = (vy + k3vy)*h

    vx += (k1vx + 2*k2vx + 2*k3vx + k4vx)/6
    x += (k1x + 2*k2x + 2*k3x + k4x)/6

    vy += (k1vy + 2*k2vy + 2*k3vy + k4vy)/6
    y += (k1y + 2*k2y + 2*k3y + k4y)/6

    if -0.001 < x < 0.001:
        if vx < 0:
            fun.color = color.red
            fun.plot(pos=(y, vy))
        if vx > 0:
            fun.color = color.blue
            fun.plot(pos=(y, vy))

    t += h
