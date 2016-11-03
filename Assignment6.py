"""
Completes Assignment 6
11/3/2016
"""
from math import sin
from numpy import arange
import matplotlib.pyplot as plt

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
    # plt.title("1 - t*sin(x) for h = " + str(h))
    # plt.xlabel('t')
    # plt.ylabel('x')
    # plt.plot(tpoints, xpoints, 'r-', label="RK4")
    # plt.plot(tpoints, epoints, 'g-', label="Euler")
    # plt.legend(loc="best")
    # plt.show()
    plt.title("Difference between RK4 and Euler for h = " + str(h))
    plt.plot(tpoints, diff, 'b-')
    plt.show()
