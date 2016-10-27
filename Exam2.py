"""
Exam1.py
Completes the second take home exam
10/27/16
"""
from math import *
import matplotlib.pyplot as plt

# Problem 1
print "Problem 1"
vt = 10
h = 0.0001
for v in (5.0, 10.0, 15.0, 20.0):
    vi = v
    y = 0
    maxy = 0
    t = 0
    trise = 0
    while y >= 0:
        ay = -9.81 * (1 + v / vt ** 2)
        v += ay * h
        y += v * h
        t += h
        if y > maxy:
            maxy = y
            trise = t
    print "For an initial velocity of {0:0.1f}m/s, the time to rise was {1:0.5f}s and the time to fall was {2:0.5f}s."\
        .format(vi, trise, t-trise)

# Problem 2
print "\nProblem 2"
def dT_dt(T, Ts): return -r*(T-Ts)
def Ts(t): return (25+10) - 10*sin(2*pi*(t+6.25)/24)
t = 0.0
T = 68.0
Tend = 0.0
tend = 0.0
r = 0.15
h = 0.1
tfreezing = 0
plt.plot(t, T, 'bo', label="Inside Temperature")
plt.plot(t, Ts(0), 'ro', label="Outside Temperature")
while t <= 24.0*6:
    Tend = T + dT_dt(T, Ts(t))*h
    tend = t + h
    T += (dT_dt(T, Ts(t)) + dT_dt(Tend, Ts(t)))/2*h
    if tfreezing == 0 and 31.8 < T < 32.2:
        tfreezing = t
    plt.plot(t, T, 'bo')
    plt.plot(t, Ts(t), 'ro')
    t += h
print "The time until Clark Hall reaches 32F is {0:.2f}h".format(tfreezing)
plt.title("Temperature")
plt.legend(loc='best')
plt.show()
