"""
binaryrk4.py
simulates a binary star system using the Runge-Kutta 4th order algorithim
"""
from visual import *
from vis import *
from math import *

# set constant values
G = 6.67e-11
AU = 1.5e11
year = 365.25 * 24. * 60. * 60

# turn autoscale on
scene.autoscale = 1

# create two star objects and a center of mass object
starA = sphere(pos=(0, 0, 0), radius=6.95e9, mass=2e30, color=color.yellow)
starB = sphere(pos=(AU, 0, 0), radius=6.95e9, mass=2e30, color=color.red)
CM = sphere(pos=(starA.pos * starA.mass + starB.pos * starB.mass) / (starA.mass + starB.mass), radius=2e9,
            color=color.green)

# set up values for determing eccentricity
Rmax = 0
Rmin = 5 * AU
L = vector(0, 0, 0)
Lrep = arrow(pos=starA.pos, axis=L, color=color.cyan)

# initialize velocities of stars and CM
starA.vel = vector(0, 1.4 * pi * AU / year, pi * AU / year)
starA.trail = curve(color=starA.color)
starB.vel = vector(0, -1.4 * pi * AU / year, -pi * AU / year)
starB.trail = curve(color=starB.color)
CM.vel = vector(0, 0, 0)

varrowA = arrow(pos=starA.pos, axis=starA.vel, length=7e9, color=color.white)
varrowB = arrow(pos=starB.pos, axis=starB.vel, length=7e9, color=color.white)
F = vector(0, 0, 0)

# initialize variables
t = 0
h = 1e4
ecc = 0
ecc_s = str("%.3f" % ecc)
v = str("%.3f" % mag(starB.vel))
velocitylabel = label(pos=starA.pos, text="vel: " + v + "\nEcc: " + ecc_s, xoffset=20, yoffset=20)


# define acceleration of a star; this can switch from one star to another cleverly
def acc(starpos):
    return -G * starother.mass * (starpos - starother.pos) / r ** 3


# Runge-Kuta 4th order algorithm
def rk4(star):
    k1v = h * acc(star.pos)
    k1x = h * star.vel

    k2v = h * acc(star.pos + k1x / 2.0)
    k2x = h * (star.vel + k1v / 2.0)

    k3v = h * acc(star.pos + k2x / 2.0)
    k3x = h * (star.vel + k2v / 2.0)

    k4v = h * acc(star.pos + k3x)
    k4x = h * (star.vel + k3v)

    star.vel += (k1v + 2.0 * k2v + 2.0 * k3v + k4v) / 6.0
    star.pos += (k1x + 2.0 * k2x + 2.0 * k3x + k4x) / 6.0


# include keyboard interactions
while true:
    if scene.kb.keys:  # check if there is a keyboard event waiting
        s = scene.kb.getkey()  # obtain keyboard entry
        if s == 'b':
            starB.vel *= 1.1
        if s == 'r':
            starB.vel *= 0.9
        if s == 'a':
            print Rmax, "\t", Rmin

    r = mag(starA.pos - starB.pos)
    for i in range(0, 2):
        if i == 1:
            starother = starB
            rk4(starA)
        else:
            r = mag(starA.pos - starB.pos)
            starother = starA
            rk4(starB)

    starA.trail.append(pos=starA.pos)
    starB.trail.append(pos=starB.pos)

    # calculate various quantities
    CM.pos = (starA.pos * starA.mass + starB.pos * starB.mass) / (starA.mass + starB.mass)
    M = starA.mass + starB.mass  # mass of the center of mass
    m = starA.mass * starB.mass / (starA.mass + starB.mass)  # reduced mass of the system
    t += h
    L = m * cross(starB.pos - starA.pos, starB.vel - starA.vel)  # angular momentum
    E = 0.5 * m * mag2(starB.vel - starA.vel) - G * M * m / r  # energy
    ecc = sqrt(1. + 2.0 * mag2(L) * E / ((G * M) ** 2 * m ** 3))  # eccentricity
    ecc_s = str("%.4f" % ecc)  # labels
    v = str("%.3f" % mag(starB.vel))
    velocitylabel.pos = CM.pos
    velocitylabel.text = "vel: " + v + "\nEcc: " + ecc_s
    R = mag(starA.pos - CM.pos)
    if R > Rmax:
        Rmax = R
    if R < Rmin:
        Rmin = R

    rate(400)

