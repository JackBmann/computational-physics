'''
fallingbody.py
calculate position and graph for a freely falling body
9/8/16
'''

from numpy import max, where
import matplotlib.pyplot as plt

#initialize and set up variables
y = []
t = []
g = 9.81

t0 = 0
y0 = 2
#v0 = input("Enter the initial velocity: ")
v0 = 12.2
ycalc = 0
tcalc = 0

#create loop for iterating our equation
while ycalc >= 0:
    ycalc = y0 + v0*tcalc - .5*g*tcalc**2
    if ycalc >= 0:
        y.append(ycalc)
        t.append(tcalc)
        #increment time for calculation
        print "Height is {0:5.2f} and Time is {1:5.2f}".format(ycalc, tcalc)
    tcalc += 0.05

print "The maximum height is {0:5.2f}".format(max(y))
print "Time to reach maximum height is {0:5.2f}".format(t[where(y == max(y))[0]])

#plot our results
plt.plot(t, y, 'r^')
plt.xlabel("Time t (s)")
plt.ylabel("Height y (m)")
plt.show()