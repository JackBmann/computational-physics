'''
pi2.py
Calculates pi^2 and prints pi formatted in 2 different ways
8/30/2016
'''
from math import pi, fabs

sum = 0.0
n = input("Enter an n value: ")
for j in range(1, n+1, 1):
    sum += 1.0/(j*j)
mypi2 = 6.0*sum
print "mypi^2 =", mypi2
print "pi^2   =", pi**2
error = fabs((mypi2 - pi**2)/(pi**2)) #fabs = floating point abs()
print "error  =", error

print "Here is pi to the 2nd decimal place: %1.2f" % pi
print "Here is pi to the 5th decimal place: %1.5f" % pi
print "Here is pi to the 10th decimal place: %1.10f" % pi

print "Here is pi to the 2nd decimal place: {0:1.2f}".format(pi)
print "Here is pi to the 5th decimal place: {0:1.5f}".format(pi)
print "Here is pi to the 10th decimal place: {0:1.10f}".format(pi)