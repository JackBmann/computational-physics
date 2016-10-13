"""
sirius.py
simulates a binary star system
10/13/16
"""
from visual import *
from vis import *

# define constants
G = 6.67E-11    # gravitational constant
AU = 1.5E11     # one astronomical distance
YEAR = 365.25*24*60*60  # year in seconds

# create two stars
starA = sphere(pos=(-AU, 0, 0), radius=10*7E8, mass=2E30, color=(1, 1, 0))
starB = sphere(pos=(AU, 0, 0), radius=5*7E8, mass=2E30, color=(1, 0, 0))

# initial conditions
starA.vel = vector(0, 1.1E4, 0)
starB.vel = vector(0, -1.1E4, 0)

# time step
h = 5E3
scene.autoscale = 1

starA.trail = curve(color=starA.color)
starB.trail = curve(color=starB.color)

# loop
while True:
    r = mag(starA.pos - starB.pos)
    F = -G*starA.mass*starB.mass*(starA.pos - starB.pos) / r**3

    starA.vel += F / starA.mass*h
    starB.vel -= F / starB.mass*h

    starA.pos += starA.vel*h
    starB.pos += starB.vel*h

    starA.trail.append(pos=starA.pos)
    starB.trail.append(pos=starB.pos)

    rate(200)
