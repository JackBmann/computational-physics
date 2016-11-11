"""
Completes Assignment 6
11/3/2016
"""
from math import sin, pi, cos
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

# Problem 4
print "\nProblem 4"
def accL(l, ll, t, tt): return (l0 + l) * tt**2 - k/m*l + g*cos(t)
def accT(l, ll, t, tt): return -1.0/(l0 + l) * (g*sin(t) + 2*ll*tt)
l = 1.0
l0 = 0.5
ll = 0.0
t = pi/4.0
tt = 0.0
k = 4.9
m = 5.0
omega0 = 0.0
g = 9.81
a = 0.0
b = 60.0
N = 1000
h = (b - a) / N
time = []
timeCounter = 0.0
lpoints = []
llpoints = []
tpoints = []
ttpoints = []
while timeCounter <= N:
    k1ll = accL(l, ll, t, tt) * h
    k1l = ll * h
    k1tt = accT(l, ll, t, tt) * h
    k1t = tt * h
    k2ll = accL(l + k1l / 2.0, ll + k1ll / 2.0, t + k1t / 2.0, tt + k1tt / 2.0) * h
    k2l = (ll + k1ll / 2.0) * h
    k2tt = accT(l + k1l / 2.0, ll + k1ll / 2.0, t + k1t / 2.0, tt + k1tt / 2.0) * h
    k2t = (tt + k1tt / 2.0) * h
    k3ll = accL(l + k2l / 2.0, ll + k2ll / 2.0, t + k2t / 2.0, tt + k2tt / 2.0) * h
    k3l = (ll + k2ll / 2.0) * h
    k3tt = accT(l + k2l / 2.0, ll + k2ll / 2.0, t + k2t / 2.0, tt + k2tt / 2.0) * h
    k3t = (tt + k2tt / 2.0) * h
    k4ll = accL(l + k3l, ll + k3ll, t + k3t, tt + k3tt) * h
    k4l = (ll + k3ll) * h
    k4tt = accT(l + k3l, ll + k3ll, t + k3t, tt + k3tt) * h
    k4t = (tt + k3tt) * h
    ll += (1 / 6.0) * (k1ll + 2.0 * k2ll + 2.0 * k3ll + k4ll)
    l += (1 / 6.0) * (k1l + 2.0 * k2l + 2.0 * k3l + k4l)
    tt += (1 / 6.0) * (k1tt + 2.0 * k2tt + 2.0 * k3tt + k4tt)
    t += (1 / 6.0) * (k1t + 2.0 * k2t + 2.0 * k3t + k4t)
    lpoints.append(l)
    llpoints.append(ll)
    tpoints.append(t)
    ttpoints.append(tt)
    time.append(timeCounter)
    timeCounter += h
fig = plt.figure()
Ax = Axes3D(fig)
Ax.plot(time, lpoints, zs=llpoints, zdir='z')
Ax.set_xlim3d(0, N)
Ax.set_ylim3d(0, 20)
Ax.set_zlim3d(-10, 10)
# plt.show()

fig = plt.figure()
Ax = Axes3D(fig)
Ax.plot(time, tpoints, zs=ttpoints, zdir='z')
Ax.set_xlim3d(0, N)
Ax.set_ylim3d(-5, 5)
Ax.set_zlim3d(-5, 5)
plt.show()
