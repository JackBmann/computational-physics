"""
threebody.py
simulates a binary star and a planet system
10/18/16
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
planet = sphere(pos=(0, AU, 0), radius=2E9, color=color.green)

# plot axes
L = 2E11
xaxis = curve(pos=[(0, 0, 0), (L, 0, 0)], color=(0.5, 0.5, 0.5))
yaxis = curve(pos=[(0, 0, 0), (0, L, 0)], color=(0.5, 0.5, 0.5))
zaxis = curve(pos=[(0, 0, 0), (0, 0, L)], color=(0.5, 0.5, 0.5))

# initial conditions
starA.vel = vector(0, 1.1E4, 0)
starB.vel = vector(0, -1.1E4, 0)
planet.vel = vector(1.2E4, 0, 0)
varrow = arrow(pos=planet.pos, axis=planet.vel, length=7E9, color=color.white)

# time step
h = 5E3
scene.autoscale = 1

starA.trail = curve(color=starA.color)
starB.trail = curve(color=starB.color)
planet.trail = curve(color=planet.color)

# loop
while True:
    r = mag(starA.pos - starB.pos)
    F = -G*starA.mass*starB.mass*(starA.pos - starB.pos) / r**3

    starA.vel += F / starA.mass*h
    starB.vel -= F / starB.mass*h

    starA.pos += starA.vel*h
    starB.pos += starB.vel*h

    rplanetA = mag(planet.pos - starA.pos)
    rplanetB = mag(planet.pos - starB.pos)

    planet.vel += (-G*starA.mass*(planet.pos - starA.pos)/rplanetA**3 -
                   G*starB.mass*(planet.pos - starB.pos)/rplanetB**3)*h
    planet.pos += planet.vel*h

    varrow.pos = planet.pos
    varrow.axis = planet.vel/mag(planet.vel)*4.0E10

    starA.trail.append(pos=starA.pos)
    starB.trail.append(pos=starB.pos)
    planet.trail.append(pos=planet.pos)

    rate(200)
