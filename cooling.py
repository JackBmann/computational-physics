""""
cooling.py
solves Newton's law of cooling
9/27/16
"""
import math
import matplotlib.pyplot as plt


# calculate slope at each point using a function
def dT_dt(T, Ts):
    return -r*(T-Ts)


def Ts(t):
    return 92 - 10*math.sin(2*math.pi*(t+3)/24)

# give initial conditions
t = 0.0
T = 74.0
Tend = 0.0
tend = 0.0
r = 0.1
h = 0.1

# plot initial values to get labels for legend
plt.plot(t, T, 'bo', label="Heun's")
plt.plot(t, Ts(0), 'ro', label="Surrounding")
# plt.plot(t, math.tan(t), 'rx', label='Analytic')

# apply Euler to find y(t)
while t <= 96.0:
    plt.plot(t, T, 'bo')
    plt.plot(t, Ts(t), 'ro')
    # plt.plot(t, math.tan(t), 'rx')
    Tend = T + dT_dt(T, Ts(t))*h
    tend = t + h
    T += (dT_dt(T, Ts(t)) + dT_dt(Tend, Ts(t)))/2*h
    t += h

plt.title("Heun's Method")
plt.legend(loc='upper left')
plt.show()
