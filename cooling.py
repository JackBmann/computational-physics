'''
cooling.py
solves Newton's law of cooling
9/27/16
'''
from math import tan
import matplotlib.pyplot as plt

#calculate slope at each point using a function
def dT_dt(T, Ts):
    return -r*(T-Ts)

#give initial conditions
t = 0
T = 90
Tend = 0
tend = 0
r = 0.32
Ts = 25
h = 0.01

#plot initial values to get labels for legend
plt.plot(t, T, 'bo', label="Heun's")
#plt.plot(t, tan(t), 'rx', label='Analytic')

#apply Euler to find y(t)
while t <= 1.0:
    plt.plot(t, T, 'bo')
    #plt.plot(t, tan(t), 'rx')
    Tend = T + dT_dt(T, Ts)*h
    tend = t + h
    T += (dT_dt(T, Ts) + dT_dt(Tend, Ts))/2*h
    t += h

plt.title("Heun's Method")
plt.legend(loc='upper left')
plt.show()
