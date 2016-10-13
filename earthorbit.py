"""
earthorbit.py
simulates Earth in its orbit
10/13/16
"""
from visual import *
from vis import *

# define constants
G = 6.67E-11    # gravitational constant
AU = 1.5E11     # one astronomical distance
YEAR = 365.25*24*60*60  # year in seconds

# create the sun and earth
sun = sphere(pos=(0, 0, 0), radius=10*7E8, mass=2E30, color=(1, 1, 0))
earth = sphere(pos=(AU, 0, 0), radius=400*6.4E6, mass=6E24, color=(0, 1, 1))

# initial conditions
earth.vel = vector(-0.5*sqrt(G*sun.mass/AU), sqrt(G*sun.mass/AU), 0)
earth.acc = vector(-G*sun.mass/AU**2, 0, 0)

# time step
h = 1E4
scene.autoscale = 1

# loop
while True:
    r = mag(earth.pos - sun.pos)

    earth.acc = -G*sun.mass*(earth.pos - sun.pos) / r**3
    earth.vel += earth.acc*h
    earth.pos += earth.vel*h

    rate(200)
