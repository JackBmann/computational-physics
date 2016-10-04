"""
curvesofpursuit.py
solves three dogs chasing each other
10/4/16
"""
from vis import *
from visual import *
from math import sin, cos, tan, pi

# create dogs
Mishka = sphere(pos=(0, 0, 0), radius=5, color=color.yellow)
Lucy = sphere(pos=(100, 0, 0), radius=5, color=color.white)
Bheru = sphere(pos=(50, 100*sin(60.0*pi/180.0), 0), radius=5, color=color.red)

# define scene
scene.center = (50, 50*tan(30.0*pi/180.0), 0)
perimeter = ring(pos=scene.center, axis=(0, 0, 1), color=color.green, radius=50/cos(30.0*pi/180.0))

h = 0.02
t = 0

# initial velocities
Mishka.vel = vector(10, 0, 0)
Lucy.vel = vector(-10*sin(60.0*pi/180.0), 10, 0)
Bheru.vel = vector(-5, -10*sin(60.0*pi/180.0), 0)

# create trails
Mishka.trail = curve(color=Mishka.color)
Lucy.trail = curve(color=Lucy.color)
Bheru.trail = curve(color=Bheru.color)

distance = 0

# pursuit
while mag(Bheru.pos - Lucy.pos) > 0.2:
    rate(100)
    Mishka.vel = 10*(Lucy.pos - Mishka.pos)/mag(Lucy.pos - Mishka.pos)
    Lucy.vel = 10*(Bheru.pos - Lucy.pos)/mag(Bheru.pos - Lucy.pos)
    Bheru.vel = 10*(Mishka.pos - Bheru.pos)/mag(Mishka.pos - Bheru.pos)

    Mishka.pos += Mishka.vel*h
    Lucy.pos += Lucy.vel*h
    Bheru.pos += Bheru.vel*h

    Mishka.trail.append(pos=Mishka.pos)
    Lucy.trail.append(pos=Lucy.pos)
    Bheru.trail.append(pos=Bheru.pos)

    distance += mag(Mishka.vel*h)
    t += h

print 'distance = {0:5.3f} and time = {1:5.3f}'.format(distance, t)
