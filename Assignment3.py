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


# Problem 4
print "\nProblem 4"


# Problem 5
print "\nProblem 5"

