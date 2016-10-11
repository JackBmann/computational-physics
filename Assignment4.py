"""
Assignment4.py
This file completes Assignment 4.
10/10/16
"""
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, pi

# Problem 1
print "Problem 1"
# R = v_0 * v_t * cos(theta) / g
v_0 = 30
v_t = 45
g = 9.81
theta = 0
max_R = 0
max_theta = 0
while theta <= 90:
    R = v_0**2 * sin(2*theta*pi/180.0) / g * 1.09361  # 1m = 1.09361yards
    if R > max_R:
        max_R = R
        max_theta = theta
    plt.plot(theta, R, 'rx')
    theta += 0.5
plt.xlabel("Launch angle (degrees)")
plt.ylabel("Range (yards)")
print "The optimal launch angle for the greatest horizontal range in the air is", max_theta, "yards"
if max_R > 80:
    print "The results agree that Dak Prescott is a capable quarterback, because he can throw:", max_R, "yards."
else:
    print "The results disagree that Dak Prescott is a capable quarterback, because he can only throw:", max_R, "yards."
plt.show()

# Problem 2
print "\nProblem 2"
height = 10
g = 9.81
v = sqrt(2*g*height)    # speed on first bounce
theta = 30*pi/180.0
vx = v*cos(theta)
vy = v*sin(theta)
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
        vy = v*sin(theta)
        vx = v*cos(theta)

    t += h

    plt.plot(x, y, 'r+')
    plt.plot(x, yincline, 'ko')

print "The distance between consecutive impact points on the plane grow exponentially."
print "Air resistance causes both the vertical and horizontal distance of each bounce to decrease."
plt.show()

# Problem 3
print "\nProblem 3"


# Problem 4
print "\nProblem 4"
mass = 0.02
g = 9.81
v = 2
x = 0
t = 0
friction = 0
xs = [x]
vs = [v]
ts = [t]
while v >= 0:
    friction = 0.4 * mass * g
    a = friction / mass
    v += -a * t
    x += v * t
    t += 0.01
    mass += 0.02
    xs.append(x)
    vs.append(v)
    ts.append(t)
    print t, x, v, a, friction, mass
print ts, xs, vs
plt.plot(ts, xs, 'bo', label="Displacement (m)")
plt.plot(ts, vs, 'r+', label="Velocity (m/s")
plt.legend(loc='best')
plt.show()
