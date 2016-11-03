"""
simpleRK4.py
solves a first order differential equation
11/1/16
"""
from math import sin
from numpy import arange
import matplotlib.pyplot as plt


# define our differential equation (slope)
def f(x, t):
    return 1 - t*sin(x)

# define the interval for the solution and grid spacing
x = 0.0
e = 0.0
a = 0.0
b = 40
N = 1000
h = (b - a) / N

# create a list of time points
tpoints = arange(a, b, h)
# create a list to populate of solution values
xpoints = []
epoints = []

for t in tpoints:
    # implement RK4
    k1 = f(x, t) * h
    k2 = f(x + 0.5*k1, t + h/2.0) * h
    k3 = f(x + 0.5*k2, t + h/2.0) * h
    k4 = f(x + k3, t + h/2.0) * h

    x += (1/6.0) * (k1 + 2.0*k2 + 2.0*k3 + k4)
    xpoints.append(x)

    e += f(e, t) * h
    epoints.append(e)

# plot solutions
plt.xlabel('t')
plt.ylabel('x')
plt.plot(tpoints, xpoints, 'r-')
plt.plot(tpoints, epoints, 'g-')
plt.show()
