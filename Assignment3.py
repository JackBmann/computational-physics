"""
Assignment3.py
This file completes Assignment 3.
9/28/16
"""
import numpy as np
import matplotlib.pyplot as plt

# Problem 1
print "Problem 1"
fig = plt.figure()
sub = plt.subplot(111)
x = [1, 2, 3, 4, 5, 6]
freq = [17, 20, 29, 20, 18, 16]
total = 0
for i in freq:
    total += i
avg = total/6
sub.bar(x, freq, 1)
sub.set_xlim(1, 7)
sub.set_ylim(0, 30)
sub.plot([1, 2, 3, 4, 5, 6, 7], [avg, avg, avg, avg, avg, avg, avg], 'r--', linewidth=1, label="Expected value")
plt.legend()
print "The die appears to be weighted to roll a 3."
plt.show()

# Problem 2
print "\nProblem 2"
t, y, tmid, ymid = 0, 0, 0, 0
h = 0.1
while t <= 2.0:
    print "y({0:5.2f}) = {1:5.2f}".format(t, y)
    ymid = y + (np.e**(-2*t) - y)*h/2.0
    tmid = t + h/2.0
    y += (np.e**(-2*t) - ymid)*h
    t += h

# Problem 3
print "\nProblem 3"
Ooriginal, O, F, Ne, t = 1000.0, 1000.0, 0.0, 0.0, 0.0
Os, Fs, Nes, ts, parentRatios, daughterRatios, FDecayRate, NeDecayRate = [], [], [], [], [], [], [], []
while t <= 60:
    Os.append(O)
    Fs.append(F)
    Nes.append(Ne)
    ts.append(t)
    parentRatios.append(O/Ooriginal)
    daughterRatios.append((F+Ne)/Ooriginal)
    FDecayRate.append(F*np.e**(-13.5*t))
    NeDecayRate.append(Ne*np.e**(-11.0*t))
    if t % 13.5 == 0:
        F += O/2.0
        O /= 2.0
    if t % 11 == 0:
        Ne += F/2.0
        F /= O
    t += 1.0
print "At time t = 60, the Parent to Parent Ratio is: {0:5.2f}, the Parent to Daughter Ratio is: {1:5.2f}, " \
      "the Decay Rate of F is: {2:5.2f}, and the Decay Rate of Ne: {3:5.2f},"\
      .format(parentRatios[60], daughterRatios[60], FDecayRate[60], NeDecayRate[60])
# plt.plot(ts, Os, "b-", label="# of O")
# plt.plot(ts, Fs, "r-", label="# of F")
# plt.plot(ts, Nes, "y-", label="# of Ne")
plt.plot(ts, parentRatios, "g-", label="Parent to Parent Ratio")
plt.plot(ts, daughterRatios, "m-", label="Parent to Daughter Ratio")
plt.plot(ts, FDecayRate, "k-", label="Decay Rate of F")
plt.plot(ts, NeDecayRate, "c-", label="Decay Rate of Ne")
plt.legend()
plt.show()

# Problem 4
print "\nProblem 4"
t, Tend, tend, equaltime, r, h = 0, 0, 0, 0, 0.1, 1
# T = input("Enter the initial temperature of the apartment: ")
T = 72
Ts = 92
time, Tvals, Tsvals = [0], [T], [Ts]
while t <= 48:
    plt.plot(t, T, 'bo')
    Tend = T + -r*(T-Ts)*h
    tend = t + h
    T += (-r*(T-Ts) + -r*(Tend-Ts))/2*h
    Ts = 92 - 10*np.sin((2*np.pi*(t-3))/24)
    t += h
    if (equaltime == 0) & (int(T) == int(Ts)):
        equaltime = t
    time.append(t)
    Tvals.append(T)
    Tsvals.append(Ts)
plt.plot(time, Tvals, "bo", label="Inside Temperature")
plt.plot(time, Tsvals, "ro", label="Outside Temperature")
plt.legend()
print "The maximum temperature reached in the apartment is: {0:5.2f} degrees F, the first time the inside temperature" \
      " equals the outside temperature is at {1:} hours, \nand the apartment temperature lags the outside temperature" \
      " by about 6 hours.".format(max(Tvals), equaltime)
plt.show()

# Problem 5
print "\nProblem 5"

