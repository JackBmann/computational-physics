"""
baseball.py
plots trajectories of pitches
9/22/16
"""
from numpy import loadtxt, zeros, array
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sin, cos, sqrt, pi, exp

# load data
data = loadtxt("FlightData.txt", skiprows=1)
ftime = data[:, 1] - data[:, 0]
tmax = 45
# number of pitches
N = len(ftime)

# get initial values
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

# step through time
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


# define our drag coefficient
def k_D(v):
    delta = 5.0
    vd = 35.0
    return 0.0039 + 0.0058 / (1.0 + exp((v - vd) / delta))


# define our algorithm
def euler(vx, vy, vz):
    x = 0
    y = 0
    z = input("Enter the pitcher's release height: ")
    t = 0
    h = 0.001
    k_L = 1.92E-4
    omega = 1800.0 * 2.0 * pi / 60.0

    # create a loop while the ball is in the air
    while x <= 18.4:
        # for plotting purposes
        X.append(x)
        Y.append(y)
        Z.append(z)

        v = sqrt(vx**2 + vy**2 + vz**2)

        # accelerations
        ax = -k_D(v)*v*vx + k_L*(vz*omega*sin(phi) - vy*omega*cos(phi))
        ay = -k_D(v)*v*vy + k_L*vx*omega*cos(phi)
        az = -k_D(v)*v*vz - k_L*vx*omega*sin(phi) - g

        # use Euler
        vx += ax*h
        vy += ay*h
        vz += az*h

        x += vx*h
        y += vy*h
        z += vz*h

        t += h

done = 0
while not done:     # input pitch type
    X = []
    Y = []
    Z = []
    pitch = raw_input("Type of pitch: fastball(f)/curveball(c)/slider(s)/screwball(w): ")
    if pitch == 'c':
        v = 34.5
        phi = 90.0*pi/180.0
    elif pitch == 's':
        v = 37.5
        phi = 45.0*pi/180.0
    elif pitch == 'w':
        v = 34.5
        phi = -90.0*pi/180.0
    else:
        v = 42.0
        phi = 0.0

    # set initial angle from horizontal
    theta = -3.0*pi/180.0

    # initial velocity components
    vx = v*cos(theta)
    vy = 0.0
    vz = v*sin(theta)

    g = 9.81

    euler(vx, vy, vz)

    # plot trajectory and strike zone
    fig = plt.figure()
    Ax = Axes3D(fig)
    Ax.plot(X, Y, zs=Z, zdir='z')   # plot path
    Ax.plot_wireframe(array([[18.4, 18.4], [18.4, 18.4]]), array([[-0.22, 0.22], [-0.22, 0.22]]),
                      array([[0.5, 0.5], [1.1, 1.1]]), color='r')
    Ax.set_xlim3d(0, 18.4)
    Ax.set_ylim3d(-1, 1)
    Ax.set_zlim3d(0, 2)
    plt.show()

    reply = raw_input("Again? (y/n) ")  # get response for rerunning
    if reply == 'n' or reply == 'N':
        print "Goodbye"
        done = 1
