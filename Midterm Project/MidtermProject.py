"""
MidtermProject.py
simulates Mercury in its orbit and includes its precession
10/17/16
"""
from visual import *
from vis import *
from math import *
import matplotlib.pyplot as plt


# returns the slope of the best fit line for the given data
def bestfitline(thetas, times):
    sum_x = 0
    sum_y = 0
    sum_xx = 0
    sum_xy = 0

    for i in range(len(thetas)):
        x = thetas[i]
        y = times[i]
        sum_x += x
        sum_y += y
        sum_xx += x * x
        sum_xy += x * y

    return (sum_xx * sum_y - sum_x * sum_xy) / (len(thetas) * sum_xx - sum_x * sum_x)

# define constants
G = -6.67E-11    # gravitational constant
AU = 1.496E11     # one astronomical distance
YEAR = 365.25*24*60*60  # year in seconds
alpha = 0.001

# create the sun and earth
sun = sphere(pos=(0, 0, 0), radius=6.957E8, mass=1.988435E30, color=color.orange)
mercury = sphere(pos=(0.47*AU, 0, 0), radius=2.4397E6, mass=3.30104E23, color=color.gray(10), make_trail=true)

# initial conditions
mercury.vel = vector(-0.5 * 8.2 * AU / YEAR, 8.2 * AU / YEAR, 0)
mercury.acc = vector(G * sun.mass * (1 + alpha / (0.47*AU)**2) / (0.47*AU)**2, 0, 0)

h = 1E4
previousthetas = []
while alpha <= 0.004:

    time = 0
    thetas = []
    times = []

    while time < 10250000:
        r = mag(mercury.pos - sun.pos)
        radial = (mercury.pos - sun.pos) / r
        theta = degrees(atan(mercury.y / mercury.x))
        F = (G * sun.mass * mercury.mass / r**2) * (1 + alpha / r**2) * radial
        mercury.acc = F / mercury.mass
        mercury.vel += mercury.acc * h
        mercury.pos += mercury.vel * h
        time += h
        thetas.append(theta)
        times.append(time)
        rate(600)

    if len(previousthetas) > 0:
        dthetas = []
        for i in range(len(thetas)):
            dthetas.append(thetas[i] - previousthetas[i])
        plt.plot(alpha, bestfitline(dthetas, times), 'ko')

    previousthetas = thetas
    alpha += 0.0005

plt.show()
