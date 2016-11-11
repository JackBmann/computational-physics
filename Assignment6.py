"""
Completes Assignment 6
11/3/2016
"""
from math import sin
from numpy import arange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Problem 1
print "Problem 1"
for h in [0.001, 0.01, 0.05]:
    x = 0.0
    e = 0.0
    tpoints = arange(0, 40, h)
    xpoints = []
    epoints = []
    diff = []
    for t in tpoints:
        k1 = (1 - t * sin(x)) * h
        k2 = (1 - (t + h/2.0) * sin(x + 0.5*k1)) * h
        k3 = (1 - (t + h / 2.0) * sin(x + 0.5 * k2)) * h
        k4 = (1 - (t + h/2.0) * sin(x + k3)) * h
        x += (1/6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
        xpoints.append(x)
        e += (1 - t * sin(e)) * h
        epoints.append(e)
        diff.append(x - e)
    plt.title("1 - t*sin(x) for h = " + str(h))
    plt.xlabel('t')
    plt.ylabel('x')
    plt.plot(tpoints, xpoints, 'r-', label="RK4")
    plt.plot(tpoints, epoints, 'g-', label="Euler")
    plt.legend(loc="best")
    plt.show()
    plt.title("Difference between RK4 and Euler for h = " + str(h))
    plt.plot(tpoints, diff, 'b-')
    plt.show()
print "RK4 is more accurate than Euler, but the differences are only noticeable with tiny time steps."

# Problem 2
print "\nProblem 2"
def acc(x, v): return -25*x - 0.05*v
x = 10.0
v = 0.0
a = 0.0
b = 60.0
N = 1000
h = (b - a) / N
tpoints = arange(a, b, h)
xpoints = []
vpoints = []
for t in tpoints:
    k1v = acc(x, v) * h
    k1x = v * h
    k2v = acc(x + k1x/2.0, v + k1v/2.0) * h
    k2x = (v + k1v/2.0) * h
    k3v = acc(x + k2x/2.0, v + k2v/2.0) * h
    k3x = (v + k2v/2.0) * h
    k4v = acc(x + k3x, v + k3v) * h
    k4x = (v + k3v) * h
    v += (1/6.0) * (k1v + 2.0*k2v + 2.0*k3v + k4v)
    x += (1/6.0) * (k1x + 2.0*k2x + 2.0*k3x + k4x)
    xpoints.append(x)
    vpoints.append(v)
fig = plt.figure()
Ax = Axes3D(fig)
Ax.plot(tpoints, xpoints, zs=vpoints, zdir='z')
Ax.set_xlim3d(0, 60)
Ax.set_ylim3d(-50, 50)
Ax.set_zlim3d(-50, 50)
plt.show()

# Problem 3
print "\nProblem 3"
def acc(x, v, t): return 100*sin(5.6*t) - 25*x - 0.05*v
x = 0.0
v = 0.0
a = 0.0
b = 60.0
N = 1000
h = (b - a) / N
tpoints = arange(a, b, h)
xpoints = []
vpoints = []
for t in tpoints:
    k1v = acc(x, v, t) * h
    k1x = v * h
    k2v = acc(x + k1x/2.0, v + k1v/2.0, t) * h
    k2x = (v + k1v/2.0) * h
    k3v = acc(x + k2x/2.0, v + k2v/2.0, t) * h
    k3x = (v + k2v/2.0) * h
    k4v = acc(x + k3x, v + k3v, t) * h
    k4x = (v + k3v) * h
    v += (1/6.0) * (k1v + 2.0*k2v + 2.0*k3v + k4v)
    x += (1/6.0) * (k1x + 2.0*k2x + 2.0*k3x + k4x)
    xpoints.append(x)
    vpoints.append(v)
fig = plt.figure()
Ax = Axes3D(fig)
Ax.plot(tpoints, xpoints, zs=vpoints, zdir='z')
Ax.set_xlim3d(0, 60)
Ax.set_ylim3d(-50, 50)
Ax.set_zlim3d(-100, 100)
print "In comparison to the Problem 2, this phase diagram is much more sporadic."
plt.show()
