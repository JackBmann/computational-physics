"""
superballonincline.py
10/6/16
"""
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, pi

# initial conditions
height = input("Enter the height above the incline the ball is released: ")
g = 9.81
v = sqrt(2*g*height)    # speed on first bounce

def bounce(vx, vy):
    x = 0
    y = 0
    t = 0
    h = 0.01

    while t < 20:
        v = sqrt(vx**2 + vy**2)
        ay = -g
        vy += ay*h
        y += vy*h
        x -= vx*h

        yincline = x*sqrt(3)/3.0
        if y <= yincline:
            print "bounce!"
            vy = v*sin(theta)
            vx = v*cos(theta)

        t += h

        plt.plot(x, y, 'r+')
        plt.plot(x, yincline, 'ko')

done = False
while not done:
    theta = 30*pi/180.0
    vx = v*cos(theta)
    vy = v*sin(theta)
    bounce(vx, vy)
    done = True
plt.show()
