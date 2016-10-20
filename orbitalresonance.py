"""
kirkwood.py
simulation of the resonances in the asteroid belt
given conditions are for a 2:1 resonance
"""
from visual import *
from math import *
from random import uniform
import matplotlib.pyplot as plt
from vis import *

# from visual.graph import*
# from visual.controls import*
# from __future__ import division

scene = display(x=0, y=0, height=800, width=800, range=1.5)
# plot = gdisplay(x=0,y=801, title='Radius v. Time', xtitle='t', ytitle='r/r0 -1')
# data = gdots(color=color.red)

eps = 9.0e-4
theta = 0
t = 0

asteroid = []
r2 = -1 * pow(2, -2. / 3.)  #
r = -1 * pow(3., -2. / 3.)
r32 = -1 * pow(1.5, -2. / 3.)  #
v2 = -pow(2, 1. / 3.)
v = -1 * pow(3., 1. / 3.)
v32 = -pow(1.5, 1. / 3.)
for i in range(0, 100):
    phi = i * 2 * pi / 100.
    asteroid.append(sphere(pos=(r * cos(phi), r * sin(phi), .01 * r), color=(.54, .39, .03), radius=0.015,
                           v=vector(-v * sin(phi), v * cos(phi), .01 * v), a=vector(0, 0, 0), ))
for i in range(0, 100):
    phi = i * 2 * pi / 100.
    asteroid.append(sphere(pos=(r2 * cos(phi), r2 * sin(phi), .01 * r), color=(.54, .39, .03), radius=0.015,
                           v=vector(-v2 * sin(phi), v2 * cos(phi), .01 * v2), a=vector(0, 0, 0), ))

for i in range(0, 100):
    phi = i * 2 * pi / 100.
    asteroid.append(sphere(pos=(r32 * cos(phi), r32 * sin(phi), .01 * r), color=(.54, .39, .03), radius=0.015,
                           v=vector(-v32 * sin(phi), v32 * cos(phi), .01 * v32), a=vector(0, 0, 0), ))

asteroid[0].color = color.green
asteroid[100].color = color.green
asteroid[200].color = color.green
sun = sphere(pos=(0, 0, 0), color=color.yellow, radius=.1)
jupiter = sphere(pos=(1, 0, 0), color=color.red, radius=.05)


# for 3:2 resonance the initial conditions are r=(3/2)^(-2./3.) and v=(3./2.)^(1./3.)

def RK():
    global asteroid, theta
    # k1x=0, k2x=0, k3x=0, k4x=0
    # k1y=0, k2y, k3y, k4y=0
    # k1vx=0, k2vx=0, k3vx=0, k4vx=0
    # k1vy=0, k2vy=0, k3vy=0, k4vy=0

    count = 0
    dt = 0.01
    global t
    # r

    while t < 100:
        # c.interact()
        # rate(500)
        for i in asteroid:
            k1vx = ax(i.x, i.y, theta) * dt
            k1vy = ay(i.x, i.y, theta) * dt

            k1x = i.v.x * dt
            k1y = i.v.y * dt

            k2vx = ax(i.x + k1x / 2, i.y + k1y / 2, theta + dt / 2) * dt
            k2vy = ay(i.x + k1x / 2, i.y + k1y / 2, theta + dt / 2) * dt

            k2x = (i.v.x + k1vx / 2) * dt
            k2y = (i.v.y + k1vy / 2) * dt

            k3vx = ax(i.x + k2x / 2, i.y + k2y / 2, theta + dt / 2) * dt
            k3vy = ay(i.x + k2x / 2, i.y + k2y / 2, theta + dt / 2) * dt

            k3x = (i.v.x + k2vx / 2) * dt
            k3y = (i.v.y + k2vy / 2) * dt

            k4vx = ax(i.x + k3x, i.y + k3y, theta + dt) * dt
            k4vy = ay(i.x + k3x, i.y + k3y, theta + dt) * dt

            k4x = (i.v.x + k3vx) * dt
            k4y = (i.v.y + k3vy) * dt

            i.v.x += (k1vx + 2 * k2vx + 2 * k3vx + k4vx) / 6
            i.v.y += (k1vy + 2 * k2vy + 2 * k3vy + k4vy) / 6

            i.x += (k1x + 2 * k2x + 2 * k3x + k4x) / 6
            i.y += (k1y + 2 * k2y + 2 * k3y + k4y) / 6

        count += 1
        if (count == 100 and t < 500):
            plt.plot(t, asteroid[0].pos.mag, 'r-')
            #   data.plot(pos=(t,asteroid[0].pos.mag-.75), color = color.red)
            #  data.plot(pos=(t,asteroid[100].pos.mag-.75), color = color.green)
            count = 0

        t += dt
        theta += dt
        jupiter.pos = (cos(theta), sin(theta), 0)


def ax(x, y, theta):
    global eps
    # d1, d2
    d1 = sqrt(x * x + y * y + 2 * (x * cos(theta) + y * sin(theta)) * eps + eps ** 2)
    d2 = sqrt(x * x + y * y - 2 * (x * cos(theta) + y * sin(theta)) * (1 - eps) + (1 - eps) ** 2)
    return -(1 - eps) * (x + eps * cos(theta)) / (d1 ** 3) - eps * (x - (1 - eps) * cos(theta)) / (d2 ** 3)


def ay(x, y, theta):
    global eps
    # d1, d2
    d1 = sqrt(x * x + y * y + 2.0 * (x * cos(theta) + y * sin(theta)) * eps + eps ** 2)
    d2 = sqrt(x * x + y * y - 2.0 * (x * cos(theta) + y * sin(theta)) * (1 - eps) + (1 - eps) ** 2)

    return -(1 - eps) * (y + eps * sin(theta)) / (d1 ** 3) - eps * (y - (1 - eps) * sin(theta)) / (d2 ** 3)


# c = controls(title='Attributes',x=800, y=0, width=40, height=300, range=20)

# def add():
#    global asteroid, t
#    asteroid.append(sphere(pos=(r*cos(t),r*sin(t),0),color=(.54,.39,.03),radius=0.015,v=vector(-v*sin(t),v*cos(t),0),a=vector(0,0,0),))
#
#
# def remove():
#    global asteroid
#    if len(asteroid)>1:
#        asteroid[len(asteroid)-1].visible=0
#        asteroid.pop()
#
#
# add_button = button(pos=(0,10), height=10, width=20, text='ADD', action=lambda: add())
# remove_button = button(pos=(0,-10), height=10, width=20, text='REMOVE', action=lambda: remove())

# Aslider = slider(pos=(-35,-10), width=5, length=20, min=.05, max=1, axis=(0,1,0), action=lambda: set())
# A_plus_button=button(pos=(-35,10), height=3, width=3, text='+', action=lambda: adjust(mslider,.05))
# A_minus_button=button(pos=(-35,-10), height=3, width=3, text='-', action=lambda: adjust(mslider,-.05))
# A_text=label(pos=(-35,-15), text='m/M = %i' % (mass_ratio*100),display=c.display,box=0,line=0)
# Aslider.value=mass_ratio

# Bslider = slider(pos=(-23,-10), width=5, length=20, min=0, max=10, axis=(0,1,0), action=lambda: set())
# B_plus_button=button(pos=(-23,10), height=3, width=3, text='+', action=lambda: adjust(x0slider,1))
# B_minus_button=button(pos=(-23,-10), height=3, width=3, text='-', action=lambda: adjust(x0slider,-1))
# B_text=label(pos=(-23,15), text='x0 = %i' % star[0].x,display=c.display,box=0,line=0)
# Bslider.value=star[0].x


RK()
plt.show()
