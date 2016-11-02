"""
oscillator.py
solve a damped oscillation, second order differential equation using RK4
11/1/16
"""
from math import sin
from numpy import arange
import matplotlib.pyplot as plt


# define our differential equation (slope)
def acc(x, v):
    return -k / m * x - 2 * beta * v

# set initial values and range
x = -5.0
v = 0.0
k = 36.0
m = 1.0
beta = 0.5
a = 0.0
b = 3.0
N = 200
h = (b - a) / N

# create a list of time points
tpoints = arange(a, b, h)
# create a list to populate of solution values
xpoints = []
vpoints = []

for t in tpoints:
    # implement RK4
    k1v = acc(x, v) * h
    k1x = v * h
    k2v = acc(x + k1x/2.0, v + k1v/2.0) * h
    k2x = (v + k1v/2.0) * h
    k3v = acc(x + k2x/2.0, v + k2v/2.0) * h
    k3x = (v + k2v/2.0) * h
    k4v = acc(x + k3x/2.0, v + k3v/2.0) * h
    k4x = (v + k3v/2.0) * h

    v += (1/6.0) * (k1v + 2.0*k2v + 2.0*k3v + k4v)
    x += (1/6.0) * (k1x + 2.0*k2x + 2.0*k3x + k4x)
    xpoints.append(x)
    vpoints.append(v)

# plot solutions
plt.xlabel('t')
plt.ylabel('x')
plt.title('Damped Oscillator x vs. t')
plt.plot(tpoints, xpoints, 'r+')
plt.show()

plt.xlabel('x')
plt.ylabel('v')
plt.title('Damped Oscillator Phase Diagram v vs. x')
plt.plot(xpoints, vpoints, 'go')
plt.show()
