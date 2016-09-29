'''
heunmethod.py
solves dy/dt = y^2 + 1 by Heun's algorithm
9/22/16
'''
from math import tan
import matplotlib.pyplot as plt

#calculate slope at each point using a function
def dy_dt(y):
    return y*y + 1

#give initial conditions
t = 0
y = 0
yend = 0
tend = 0

#get user to input time step h
h = input("Enter the time step: ")

#plot initial values to get labels for legend
plt.plot(t, y, 'bo', label="Heun's")
plt.plot(t, tan(t), 'rx', label='Analytic')

#apply Euler to find y(t)
while t <= 1.0:
    plt.plot(t, y, 'bo')
    plt.plot(t, tan(t), 'rx')
    yend = y + dy_dt(y)*h
    tend = t + h
    y += (dy_dt(y) + dy_dt(yend))/2 * h
    print y - tan(t)
    t += h

plt.title("Heun's Method")
plt.legend(loc='upper left')
plt.show()
