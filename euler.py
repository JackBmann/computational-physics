'''
euler.py
solves dy/dt = y^2 + 1 by Euler midpoint algorithm
9/20/16
'''
from math import tan
import matplotlib.pyplot as plt

#calculate slope at each point using a function
def dy_dt(y):
    return y*y + 1

#give initial conditions
t = 0
y = 0
tmid = 0
ymid = 0

#get user to input time step h
h = input("Enter the time step: ")

#plot initial values to get labels for legend
plt.plot(t, y, 'bo', label='Euler')
plt.plot(t, tan(t), 'rx', label='Analytic')

#apply Euler to find y(t)
while t <= 1.0:
    plt.plot(t, y, 'bo')
    plt.plot(t, tan(t), 'rx')
    ymid = y + dy_dt(y)*h/2.0
    tmid = t + h/2.0
    y += dy_dt(ymid)*h
    t += h

plt.title('Euler Midpoint Method')
plt.legend(loc='upper left')
plt.show()
