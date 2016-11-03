"""
oscillator.py
solve a damped oscillation, second order differential equation using RK4
11/1/16
"""
from math import sin, exp
from numpy import arange
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# define our differential equation
def dx_dt(x, y):
    return exp(-0.002*t) - 0.08*x - x*y**2


def dy_dt(x, y):
    return 0.08*x - y + x*y**2

# set initial values and range
x = 0.0
y = 0.0
a = 0.0
b = 1000.0
N = 10000
h = (b - a) / N

# create a list of time points
tpoints = arange(a, b, h)
# create a list to populate of solution values
xpoints = []
ypoints = []

for t in tpoints:
    # implement RK4
    k1y = dy_dt(x, y) * h
    k1x = dx_dt(x, y) * h
    k2y = dy_dt(x + k1x / 2.0, y + k1y / 2.0) * h
    k2x = dx_dt(x + k1x / 2.0, y + k1y / 2.0) * h
    k3y = dy_dt(x + k2x / 2.0, y + k2y / 2.0) * h
    k3x = dx_dt(x + k2x / 2.0, y + k2y / 2.0) * h
    k4y = dy_dt(x + k3x, y + k3y) * h
    k4x = dx_dt(x + k3x, y + k3y) * h

    y += (1 / 6.0) * (k1y + 2.0 * k2y + 2.0 * k3y + k4y)
    x += (1/6.0) * (k1x + 2.0*k2x + 2.0*k3x + k4x)
    xpoints.append(x)
    ypoints.append(y)

fig = plt.figure()
Ax = Axes3D(fig)
Ax.plot(tpoints, xpoints, zs=ypoints, zdir='z')
Ax.set_xlim3d(0, 1000)
Ax.set_ylim3d(0, 2.5)
Ax.set_zlim3d(0, 2.5)

# plot solutions
# plt.xlabel('t')
# plt.ylabel('x')
# plt.title('Damped Oscillator x vs. t')
plt.plot(tpoints, xpoints, 'r-')
# plt.show()
#
# plt.xlabel('x')
# plt.ylabel('v')
# plt.title('Damped Oscillator Phase Diagram v vs. x')
# plt.plot(xpoints, vpoints, 'g-')
plt.show()
