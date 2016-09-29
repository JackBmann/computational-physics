'''
baseball.py
plots trajectories of pitches
9/22/16
'''
from numpy import loadtxt, zeros
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#load data
data = loadtxt("FlightData.txt", skiprows=1)
ftime = data[:, 1] - data[:, 0]
tmax = 45
#number of pitches
N = len(ftime)

#get initial values
x = data[:, 2]
y = data[:, 3]
z = data[:, 4]

vx = data[:, 5]
vy = data[:, 6]
vz = data[:, 7]

accx = data[:, 8]
accy = data[:, 9]
accz = data[:, 10]

t = 0
h = tmax/100.0

fig = plt.figure()
ax = fig.gca(projection='3d')

#step through time
for i in range(0, N):
    xplot = zeros(45, float)
    yplot = zeros(45, float)
    zplot = zeros(45, float)

    x0 = x[i]
    y0 = y[i]
    z0 = z[i]

    vx0 = vx[i]
    vy0 = vy[i]
    vz0 = vz[i]

    ax0 = accx[i]
    ay0 = accy[i]
    az0 = accz[i]

    for j in range(0, 45):
        t = j/100.0
        xplot[j] = x0 + vx0*t + 0.5*ax0*t**2
        yplot[j] = y0 + vy0*t + 0.5*ay0*t**2
        zplot[j] = x0 + vz0*t + 0.5*az0*t**2

    ax.plot(xplot, yplot, zplot)

plt.plot([0.75, 0.75, -0.75, -0.75, 0.75], [0, 0, 0, 0, 0], [-3.5, -6, -6, -3.5, -3.5])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
