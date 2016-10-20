"""
singleasteroid.py
examine resonance effects for an asteroid due to Jupiter
10/20/16
"""
from __future__ import division
from visual import *
from visual.graph import *
from vis import *

G = 6.67E-11    # gravitational constant
AU = 1.5E11     # one astronomical distance
YEAR = 365.25*24*60*60  # year in seconds

# set initial position of asteroid
r0 = 5.2*AU/pow(2, 2/3)

# create the sun, Jupiter, and an asteroid
sun = sphere(pos=(0, 0, 0), radius=100*7E8, mass=2E30, color=(1, 1, 0))
jupiter = sphere(pos=(5.2*AU, 0, 0), radius=800*6.4E7, mass=9E25, color=color.magenta)
asteroid = sphere(pos=(r0, 0, 0), radius=300*6.4E7, mass=6.025E23, color=color.green)

# initialize graphs
plot = gdisplay(x=0, y=0, height=400, width=600, title="Fractional Change vs. t",
                xtitle="time", ytitle="fractional change")
data = gcurve(color=color.white)

# initialize asteroid and jupiter
jupiter.vel = vector(0, sqrt(G*sun.mass/(5.2*AU)), 0)
asteroid.vel = vector(0, sqrt(G*sun.mass/r0), 0)
h = 1E6
t = 0

# animation
while True:
    rAJ = mag(asteroid.pos - jupiter.pos)

    asteroid.acc = -G*sun.mass*(asteroid.pos-sun.pos)/mag(asteroid.pos-sun.pos)**3 +\
                   -G*jupiter.mass*(asteroid.pos-jupiter.pos)/rAJ**3
    asteroid.vel += asteroid.acc * h
    asteroid.pos += asteroid.vel * h

    jupiter.acc = -G*sun.mass*(jupiter.pos-sun.pos)/mag(jupiter.pos-sun.pos)**3
    jupiter.vel += jupiter.acc * h
    jupiter.pos += jupiter.vel * h

    data.plot(pos=(t/YEAR, mag(asteroid.pos)/r0 - 1))

    t += h

    rate(400)
