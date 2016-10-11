"""
Assignment4.py
This file completes Assignment 4.
10/10/16
"""
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, pi

# Problem 1
print "Problem 1"
# Without Air Resistance
# # R = v_0 * v_t * cos(theta) / g
# v_0 = 30
# v_t = 45
# g = 9.81
# theta = 0
# max_R = 0
# max_theta = 0
# while theta <= 90:
#     R = v_0**2 * sin(2*theta*pi/180.0) / g * 1.09361  # 1m = 1.09361yards
#     if R > max_R:
#         max_R = R
#         max_theta = theta
#     plt.plot(theta, R, 'rx')
#     theta += 0.5

# With Air Resistance
def range(y, vx, vy, vt):
    g = 9.81
    t = 0
    x = 0
    h = 0.01
    while y >= 0:
        v = sqrt(vx**2 + vy**2)
        ay = -g*(1 + vy*v/vt**2)
        ax = -g*vx*v/vt**2
        vy += ay*h
        vx += ax*h
        y += vy*h
        x += vx*h
        t += h
    return x

v = 30
v_t = 45
theta = 0
max_R = 0
max_theta = 0
y = 0
while theta <= 90:
    v_x = v * cos(theta * pi / 180.0)
    v_y = v * sin(theta * pi / 180.0)
    x = range(y, v_x, v_y, v_t)
    plt.plot(theta, x, 'rx')
    if x > max_R:
        max_R = x
        max_theta = theta
    theta += 0.5

plt.xlabel("Launch angle (degrees)")
plt.ylabel("Range (yards)")
print "The optimal launch angle for the greatest horizontal range in the air is", max_theta, "degrees"
if max_R > 80:
    print "The results agree that Dak Prescott is a capable quarterback, because he can throw:", \
        max_R * 1.09361, "yards."
else:
    print "The results disagree that Dak Prescott is a capable quarterback, because he can only throw:", \
        max_R * 1.09361, "yards."
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
mass = 0.002
g = 9.81
v = 2
x = 0
t = 0
h = 0.001
friction = 0
xs = [x]
vs = [v]
ts = [t]
while v >= 0:
    friction = 0.4 * mass * g
    a = friction / mass
    v += -a * h
    x += v * h
    t += h
    mass += 2 * h
    xs.append(x)
    vs.append(v)
    ts.append(t)
plt.plot(ts, xs, 'b--', label="Displacement (m)")
plt.plot(ts, vs, 'r-', label="Velocity (m/s")
plt.legend(loc='best')
plt.show()
