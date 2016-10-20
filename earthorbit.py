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
earth.trail = curve(color=earth.color)
counter = 0     # for printing values
L = vector(0, 0, 0)     # angular momentum vector
rmin = AU
rmax = 0

# time step
h = 1E4
scene.autoscale = 1

# loop
while True:
    if scene.kb.keys:   # is there an event waiting to be processed?
        s = scene.kb.getkey()   # obtain keyboard information
        if s == 'b':
            earth.vel *= 1.1
            rmax = 0
            rmin = AU

    r = mag(earth.pos - sun.pos)
    if r > rmax:
        rmax = r
    if r < rmin:
        rmin = r
    L = earth.mass*cross(earth.pos, earth.vel)
    E = 0.5*earth.mass*dot(earth.vel, earth.vel) - G*sun.mass*earth.mass/r
    ecc = sqrt(1.0 + (2*dot(L, L)*E)/((G*sun.mass)**2*earth.mass**3))
    a = (rmax + rmin)/2.0
    P = sqrt(4.0*pi**2*a**3/(G*sun.mass))/YEAR

    earth.acc = -G*sun.mass*(earth.pos - sun.pos) / r**3
    earth.vel += earth.acc*h
    earth.pos += earth.vel*h
    earth.trail.append(earth.pos)

    if counter >= 1000:
        print "Mag. of Ang. Mom = {0:8.3e}, Energy = {1:8.3e}, Period = {2:8.3e}, Eccentricity = {3:8.3e}"\
            .format(mag(L), E, P, ecc)
        counter = 0

    counter += 1
    rate(200)
