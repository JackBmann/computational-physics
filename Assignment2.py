'''
Assignment2.py
This file completes Assignment 2.
9/13/16
version 1.0
'''
import numpy as np
import matplotlib.pyplot as plt
import math

#Problem 1
print "Problem 1"
#y(t) = v0*t - 1/2*g*t^2
v0 = 20.0
g = 9.81
y = []
t = []
g = 9.81
ycalc = 0
tcalc = 0
while ycalc >= 0:
    ycalc = v0*tcalc - .5*g*tcalc**2
    if ycalc >= 0:
        y.append(ycalc)
        t.append(tcalc)
    tcalc += .1
print "The maximum y position is {0:5.2f} @ {1:5.2f} seconds.".format(max(y), t[y.index(max(y))])
plt.plot(t, y, 'k.')
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.show()

#Problem 2
print "Problem 2"
def calcy(v0):
    y = []
    t = []
    g = 9.81
    ycalc = 0
    tcalc = 0
    while ycalc >= 0:
        ycalc = v0*tcalc - .5*g*tcalc**2
        if ycalc >= 0:
            y.append(ycalc)
            t.append(tcalc)
        tcalc += .1
    print "The maximum y position is {0:5.2f} @ {1:5.2f} seconds.".format(max(y), t[y.index(max(y))])
    return y, t

y5, t5 = calcy(5)
y15, t15 = calcy(15)
y20, t20 = calcy(20)
y25, t25 = calcy(25)
plt.plot(t5, y5, 'yo', label='v0 = 5')
plt.plot(t15, y15, 'ro', label='v0 = 15')
plt.plot(t20, y20, 'ko', label='v0 = 20')
plt.plot(t25, y25, 'go', label='v0 = 25')
plt.legend(loc='upper left')
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.show()

#Problem 3
print "Problem 3"
#G(x) = (1/(o*sqrt(2pi)^e))^(-x^2/2o^2)
def gaus(s):
    gs = []
    xs = []
    x = -5
    while x <= 5:
        gs.append(1.0/(s*math.sqrt(2*math.pi))*math.e**(- x**2/2*s**2))
        xs.append(x)
        x += .1
    return gs, xs
g5, x5 = gaus(0.5)
g1, x1 = gaus(1.0)
g2, x2 = gaus(2.0)
plt.plot(x5, g5, 'ko', label='sigma = 0.5')
plt.plot(x1, g1, 'ro', label='sigma = 1.0')
plt.plot(x2, g2, 'yo', label='sigma = 2.0')
plt.legend(loc='upper left')
plt.xlabel("G(x)")
plt.ylabel("x")
print "Sigma alters the height of the distribution curve at x=0."
plt.show()

#Problem 4
print "Problem 4"
n = 20
s = 2
geiger = [10, 12, 15, 8, 13, 14, 19, 18, 11, 13, 7, 8, 11, 8, 12, 6, 13, 8, 6]
ourbins = np.arange(np.floor(min(geiger)), np.ceil(max(geiger))+2, 1)
plt.hist(geiger, bins=ourbins)
sum = 0.0
for g in geiger:
    sum += g
mean = sum/n
sum_squares = 0.0
for x in geiger:
    sum_squares += (x - mean)**2
std = math.sqrt(sum_squares/n)
print "The average of the readings is {0:5.2f} and the standard deviation is {1:5.2f}".format(mean, std)
plt.show()

#Problem 5
print "Problem 5"
masses = [.2, .3, .4, .5, .6, .7, .8, .9]
spring = [4.9, 5.3, 5.7, 6.7, 7.2, 7.5, 8.4, 9.2]
g = 9.81
N = 8
sum_mass = 0
sum_spring = 0
sum_masses = 0
sum_massspring = 0
mass_max = 0
for i in range(0, N):
    if masses[i] > mass_max:
        mass_max = masses[i]
    plt.plot(masses, spring, "bx")
    sum_mass += masses[i]
    sum_spring += spring[i]
    sum_masses += masses[i]**2
    sum_massspring += masses[i]*spring[i]
A = (sum_masses*sum_spring - sum_mass*sum_massspring)/(N*sum_masses - sum_mass*sum_mass)
B = (N*sum_massspring - sum_mass*sum_spring)/(N*sum_masses - sum_mass*sum_mass)
mass_calc = np.linspace(0, mass_max, 20)
spring_calc = A + B*mass_calc
plt.plot(mass_calc, spring_calc, "r-")
y0 = A
k = (masses[1]*g)/(y[1] - y0)
print "k is {0:5.2f} and y0 is {1:5.2f}.".format(k, y0)
plt.show()

#Problem 6
print "Problem 6"
g = 9.81
time = [0]
ypos = [0.4]
data = np.loadtxt("karate.txt", skiprows=1)
time = data[:, 0]
ypos = data[:, 1]
vel = [0]
accel = [0]
for v in range(1, len(time)):
    vel.append((ypos[v] - ypos[v-1])/(time[v] - time[v-1]))
for a in range(1, len(vel)):
    accel.append((vel[a] - vel[a-1])/(time[a] - time[a-1]))
np.savetxt("karateCalcData.txt", (time, vel, accel), fmt="%5.5f")
plt.figure(1)
plt.subplot(311)
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.plot(time, ypos, 'k-')
plt.subplot(312)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.plot(time, vel, 'k-')
plt.subplot(313)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.plot(time, accel, 'k-')
maxv = max(vel)
yatmaxv = ypos[vel.index(maxv)]
if max(accel) > abs(min(accel)):
    maxa = max(accel)
    yatmaxa = ypos[accel.index(maxa)]
else:
    maxa = abs(min(accel))
    yatmaxa = ypos[accel.index(maxa * -1)]
print "The max velocity of the hand is:", maxv
print "The y position of the hand when max velocity is reached is:", yatmaxv
print "The max acceleration value of the hand is:", maxa, "or", maxa/g, "g's"
print "The y position of the hand when max acceleration value is reached is:", yatmaxa
plt.show()
