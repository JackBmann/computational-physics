"""
Assignment5.py
This file completes Assignment 5.
10/24/16
"""
from __future__ import division
from visual import *
from math import *
from random import uniform
import matplotlib.pyplot as plt
from vis import *
from visual.graph import*
from visual.controls import*

# Problem 1
print "Problem 1"
Mishka = sphere(pos=(0, 0, 0), radius=5, color=color.yellow, make_trail=true)
Lucy = sphere(pos=(200, 0, 0), radius=5, color=color.white, make_trail=true)
Bheru = sphere(pos=(100, 200*sin(60.0*pi/180.0), 0), radius=5, color=color.red, make_trail=true)
scene.center = (100, 100*tan(30.0*pi/180.0), 0)
perimeter = ring(pos=scene.center, axis=(0, 0, 1), color=color.green, radius=100/cos(30.0*pi/180.0))
h = 0.02
t = 0
Mishka.vel = vector(15, 0, 0)
Lucy.vel = vector(-15*sin(60.0*pi/180.0), 15, 0)
Bheru.vel = vector(-7.5, -15*sin(60.0*pi/180.0), 0)
distance = 0
while mag(Bheru.pos - Lucy.pos) > 0.3:
    rate(100)
    Mishka.vel = 15*(Lucy.pos - Mishka.pos)/mag(Lucy.pos - Mishka.pos)
    Lucy.vel = 15*(Bheru.pos - Lucy.pos)/mag(Bheru.pos - Lucy.pos)
    Bheru.vel = 15*(Mishka.pos - Bheru.pos)/mag(Mishka.pos - Bheru.pos)
    Mishka.pos += Mishka.vel*h
    Lucy.pos += Lucy.vel*h
    Bheru.pos += Bheru.vel*h
    distance += mag(Mishka.vel*h)
    t += h
print 'The time that elapses until the hounds meet is {1:5.3f}s and the distance each hound travels is {0:5.3f}m.'\
        .format(t, distance)

# Problem 2
print "\nProblem 2"
G = 6.67E-11
AU = 1.5E11
YEAR = 365.25*24*60*60
centerOfMass = sphere(pos=(0, 0, 0), radius=0, mass=2E30, color=(1, 1, 0), make_trail=true)
starA = sphere(pos=(AU, 0, 0), radius=400 * 6.4E6, mass=6E24, color=(0, 1, 1), make_trail=true)
starB = sphere(pos=(2*AU, 0, 0), radius=400 * 6.4E6, mass=6E24, color=(1, 1, 0), make_trail=true)
starA.vel = vector(-0.5 * sqrt(G * centerOfMass.mass / AU), sqrt(G * centerOfMass.mass / AU), 0)
starB.vel = vector(-0.5 * sqrt(G * centerOfMass.mass / (2*AU)), sqrt(G * centerOfMass.mass / (2*AU)), 0)
starA.acc = vector(-G * centerOfMass.mass / AU ** 2, 0, 0)
starB.acc = vector(-G * centerOfMass.mass / (2*AU) ** 2, 0, 0)
counter = 0
maxCounter = 15000
LA = vector(0, 0, 0)
rminA = AU
rmaxA = 0
LB = vector(0, 0, 0)
rminB = 2*AU
rmaxB = 0
h = 1E4
scene.autoscale = 1
while counter < maxCounter:
    rA = mag(starA.pos - centerOfMass.pos)
    if rA > rmaxA:
        rmaxA = rA
    if rA < rminA:
        rminA = rA
    rB = mag(starB.pos - centerOfMass.pos)
    if rB > rmaxB:
        rmaxB = rB
    if rB < rminB:
        rminB = rB
    LA = starA.mass * cross(starA.pos, starA.vel)
    EA = 0.5 * starA.mass * dot(starA.vel, starA.vel) - G * centerOfMass.mass * starA.mass / rA
    eccA = sqrt(1.0 + (2 * dot(LA, LA) * EA) / ((G * centerOfMass.mass) ** 2 * starA.mass ** 3))
    aA = (rmaxA + rminA) / 2.0
    PA = sqrt(4.0 * pi ** 2 * aA ** 3 / (G * centerOfMass.mass)) / YEAR
    LB = starB.mass * cross(starB.pos, starB.vel)
    EB = 0.5 * starB.mass * dot(starB.vel, starB.vel) - G * centerOfMass.mass * starB.mass / rB
    eccB = sqrt(1.0 + (2 * dot(LB, LB) * EB) / ((G * centerOfMass.mass) ** 2 * starB.mass ** 3))
    aB = (rmaxB + rminB) / 2.0
    PB = sqrt(4.0 * pi ** 2 * aB ** 3 / (G * centerOfMass.mass)) / YEAR
    starA.acc = -G * centerOfMass.mass * (starA.pos - centerOfMass.pos) / rA ** 3
    starB.acc = -G * centerOfMass.mass * (starB.pos - centerOfMass.pos) / rB ** 3
    starA.vel += starA.acc * h
    starB.vel += starB.acc * h
    starA.pos += starA.vel * h
    starB.pos += starB.vel * h
    if counter == maxCounter-1:
        print "The Period of rotation for StarA and StarB, respectfully, are: {0:8.3e}, {1:8.3e}".format(PA, PB)
        print "The Semi-Major Axis for StarA and StarB, respectfully, is: {0:8.3e}, {1:8.3e}".format(aA, aB)
        print "The Eccentricity for StarA and StarB, respectfully, are: {0:8.3e}, {1:8.3e}".format(eccA, eccB)
    counter += 1
    rate(600)

# Problem 3
print "\nProblem 3"
scene = display(x=0, y=0, height=800, width=800, range=1.5)
plot = gdisplay(x=0, y=801, title='Radius v. Time', xtitle='t', ytitle='r/r0 -1')
data = gdots(color=color.red)
eps = 9.0e-4
theta = 0
t = 0
asteroid = []
r2 = -1 * pow(2, -2. / 3.)
r = -1 * pow(3., -2. / 3.)
r32 = -1 * pow(1.5, -2. / 3.)
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


def RK():
    global asteroid, theta
    count = 0
    dt = 0.01
    global t
    while t < 100:
        rate(500)
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
        if count == 100 and t < 500:
            data.plot(pos=(t, asteroid[0].pos.mag-.75), color=color.red)
            data.plot(pos=(t, asteroid[100].pos.mag-.75), color=color.green)
            count = 0
        t += dt
        theta += dt
        jupiter.pos = (cos(theta), sin(theta), 0)


def ax(x, y, theta):
    global eps
    d1 = sqrt(x * x + y * y + 2 * (x * cos(theta) + y * sin(theta)) * eps + eps ** 2)
    d2 = sqrt(x * x + y * y - 2 * (x * cos(theta) + y * sin(theta)) * (1 - eps) + (1 - eps) ** 2)
    return -(1 - eps) * (x + eps * cos(theta)) / (d1 ** 3) - eps * (x - (1 - eps) * cos(theta)) / (d2 ** 3)


def ay(x, y, theta):
    global eps
    d1 = sqrt(x * x + y * y + 2.0 * (x * cos(theta) + y * sin(theta)) * eps + eps ** 2)
    d2 = sqrt(x * x + y * y - 2.0 * (x * cos(theta) + y * sin(theta)) * (1 - eps) + (1 - eps) ** 2)
    return -(1 - eps) * (y + eps * sin(theta)) / (d1 ** 3) - eps * (y - (1 - eps) * sin(theta)) / (d2 ** 3)

RK()

# Problem 4
print "\nProblem 4"
scene = display(x=0, y=0, height=800, width=800, range=1.5)
plot = gdisplay(x=0, y=801, title='Radius v. Time', xtitle='t', ytitle='r/r0 -1')
data = gdots(color=color.red)
eps = 9.0e-4
theta = 0
t = 0
asteroid = []
r2 = -1 * pow(2, -2. / 3.)
r = -1 * pow(3. / 2., -2. / 3.)
r32 = -1 * pow(1.5, -2. / 3.)
v2 = -pow(2, 1. / 3.)
v = -1 * pow(3. / 2., 1. / 3.)
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
saturn = sphere(pos=(0, 0, 0), mass=5.69E26, color=color.yellow, radius=.1)
iapetus = sphere(pos=(1, 0, 0), mass=1.88E21, color=color.red, radius=.05)


# for 3:2 resonance the initial conditions are r=(3/2)^(-2./3.) and v=(3./2.)^(1./3.)
def RK():
    global asteroid, theta
    count = 0
    dt = 0.01
    global t
    while t < 100:
        rate(500)
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
        if count == 100 and t < 500:
            data.plot(pos=(t, asteroid[0].pos.mag-.75), color=color.red)
            data.plot(pos=(t, asteroid[100].pos.mag-.75), color=color.green)
            count = 0
        t += dt
        theta += dt
        iapetus.pos = (cos(theta), sin(theta), 0)


def ax(x, y, theta):
    global eps
    d1 = sqrt(x * x + y * y + 2 * (x * cos(theta) + y * sin(theta)) * eps + eps ** 2)
    d2 = sqrt(x * x + y * y - 2 * (x * cos(theta) + y * sin(theta)) * (1 - eps) + (1 - eps) ** 2)
    return -(1 - eps) * (x + eps * cos(theta)) / (d1 ** 3) - eps * (x - (1 - eps) * cos(theta)) / (d2 ** 3)


def ay(x, y, theta):
    global eps
    d1 = sqrt(x * x + y * y + 2.0 * (x * cos(theta) + y * sin(theta)) * eps + eps ** 2)
    d2 = sqrt(x * x + y * y - 2.0 * (x * cos(theta) + y * sin(theta)) * (1 - eps) + (1 - eps) ** 2)
    return -(1 - eps) * (y + eps * sin(theta)) / (d1 ** 3) - eps * (y - (1 - eps) * sin(theta)) / (d2 ** 3)

RK()
