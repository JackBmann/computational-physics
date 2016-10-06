"""
projectile.py
10/6/16
"""
import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt

# define global parameters
g = 9.81    # SI units, magnitude of gravitational acceleration


# define an euler function to solve Newton's 2nd law and also plot
def euler(y, vx, vy, vt):
    # initialize
    t = 0
    x = 0
    h = 0.01
    height = []
    plt.xlabel("x in meters")
    plt.ylabel("y in meters")
    while y >= 0:
        # using Newtonian drag force
        v = sqrt(vx**2 + vy**2)
        ay = -g*(1 + vy*v/vt**2)
        ax = -g*vx*v/vt**2
        # use Euler's method
        vy += ay*h
        vx += ax*h
        y += vy*h
        x += vx*h
        plt.plot(x, y, 'ro')
        height.append(y)
        t += h
    print "Maximum height reached is {0:5.2f}m and time in the air is {1:5.2f}".format(max(height), t)

# loop for running various values
done = 0
while not done:
    # get initial values
    y, v, theta = input("Enter initial height, initial speed, and angle in degrees (separated by commas): ")
    vx = v*cos(theta*pi/180.0)  # convert to radians and take cosine
    vy = v*sin(theta*pi/180.0)
    vt = input("Enter the terminal velocity (in m/s): ")

    euler(y, vx, vy, vt)

    plt.show()
    reply = raw_input("Run again?  Enter y or n: ")
    if reply == 'n':
        done = 1
        print "Thank you.  See you at the ball game."
