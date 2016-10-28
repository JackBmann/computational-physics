"""
Exam1.py
Completes the second take home exam
10/27/16
"""
from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Problem 1
print "Problem 1"
vt = 10.0
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
# Part A
t = 0.0
T = 68.0
Ts = 25.0
Tend = 0.0
tend = 0.0
r = 0.15
h = 0.1
tfreezing = 0
plt.plot(t, T, 'bo', label="Inside Temperature")
plt.plot(t, 25, 'ro', label="Outside Temperature")
while t <= 48.0:
    Tend = T + -r*(T-Ts)*h
    tend = t + h
    T += (-r*(T-Ts) + -r*(Tend-Ts))/2*h
    if tfreezing == 0 and 31.8 < T < 32.2:
        tfreezing = t
    plt.plot(t, T, 'bo')
    plt.plot(t, 25, 'ro')
    t += h
# Part B
print "Parts A and B: The time until Clark Hall reaches 32F is {0:.2f}h".format(tfreezing)
plt.title("Indoor Temperature changing with a constant Outdoor Temperature")
plt.xlabel("Time (hr)")
plt.ylabel("Temperature (F)")
plt.legend(loc='best')
plt.show()

# Part C
def dT_dt(T, Ts): return -r*(T-Ts)
def Ts(t): return 20*(1 + 0.5*sin(t / 8))
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
# Part D
print "Parts C and D: The time until Clark Hall reaches 32F is {0:.2f}h".format(tfreezing)
plt.title("Indoor Temperature changing with a fluctuating Outdoor Temperature")
plt.xlabel("Time (hr)")
plt.ylabel("Temperature (F)")
plt.show()

# Problem 3
print "\nProblem 3"
# Part A
g = 9.81
dragcoeff = 0.3
density = 1.2754
radius = 0.02135
mass = 0.04593
kD = dragcoeff*density*(4*pi*radius**2) / (2.0*mass)
print "Part A: The constant factor k_D is {0:f}.".format(kD)

# Part B
kL = 1.72E-3
phi = 0.0
print "Part B: The angle phi between the spin direction and the vertical direction should be {:.2f}.".format(phi)


# Part C
print "Part C:"
def graph(theta, omega, v0):
    X = []
    Y = []
    Z = []
    vx = v0 * cos(theta)
    vy = abs(v0 * sin(theta))
    vz = 0
    x = 0
    y = 0
    z = 0
    t = 0
    h = 0.001
    while y >= 0:
        X.append(x)
        Y.append(y)
        Z.append(z)
        v = sqrt(vx**2 + vy**2 + vz**2)
        ax = -kD*v*vx + kL*(vz*omega*sin(phi) - vy*omega*cos(phi))
        ay = -kD*v*vy + kL*vx*omega*cos(phi)
        az = -kD*v*vz - kL*vx*omega*sin(phi) - g
        vx += ax*h
        vy += ay*h
        vz += az*h
        x += vx*h
        y += vy*h
        z += vz*h
        t += h
    fig = plt.figure()
    Ax = Axes3D(fig)
    Ax.plot(X, Y, zs=Z, zdir='z')
    print "The horizontal range of the trajectory of the golf ball is {:.5f}m.".format(abs(x))
    plt.show()

graph(8, 3600, 134)
graph(23, 7200, 105)
graph(45, 10800, 90)

# Problem 4
print "\nProblem 4"

