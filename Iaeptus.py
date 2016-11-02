"""
Iaeptus.py
models the orbit of Iaeptus around Saturn
"""

from __future__ import division
from visual import *
from visual.graph import *
from vis import *

G = 6.67E-12    # gravitational
AU = 1.5E11     # one astronomical distance
YEAR = 365.25*24*60*60  # year in seconds

# set initial position of asteroid
r0 = 5.2*AU/pow(2, 2/3)

# create Saturn and Iaeptus
Saturn = sphere(pos=(0, 0, 0), radius=7E8, mass=5.7E26, color=(1, 1, 0))
Iaeptus = sphere(pos=(0.02374 * AU, 0, 0), radius=2*6.4E7, mass=1.88E21, color=color.magenta)
ring = sphere(pos=Iaeptus.pos*(2./3.)**(2./3.), radius=6.4E7, mass=6E23, color=color.green)

# initialize graphs
plot = gdisplay(x=0, y=0, height=400, width=600, title='Fractional Change vs. t',
                xtitle='time', ytitle='fractional change')
data = gcurve(color=color.white)

# initialize asteroid and jupiter
Iaeptus.vel = vector(0, sqrt(G * Saturn.mass / (0.02374 * AU)), 0)
ring.vel = vector(0, sqrt(G * Saturn.mass / (mag(Iaeptus.pos)*(2./3.)**(2./3.))), 0)
initialring = 0.02374*AU*(2./3)**(2./3)
h = 1E5
t = 0
Pr = 0
PI = 0
while True:
    rAJ = mag(ring.pos - Iaeptus.pos)

    ring.acc = -G * Saturn.mass * (ring.pos - Saturn.pos) / (mag(ring.pos - Saturn.pos) ** 3) - \
                G * Iaeptus.mass * (ring.pos - Iaeptus.pos) / rAJ ** 3
    ring.vel += ring.acc * h
    ring.pos += ring.vel * h

    Iaeptus.acc = -G * Saturn.mass * (Iaeptus.pos - Saturn.pos) / (mag(Iaeptus.pos - Saturn.pos) ** 3)

    Iaeptus.vel += Iaeptus.acc * h
    Iaeptus.pos += Iaeptus.vel * h

    data.plot(pos=(t / YEAR, mag(ring.pos) / initialring - 1))
    t += h
    rate(400)
