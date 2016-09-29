""""
decay_odeint.py
solve decay problem by odeint
9/29/16
"""
from numpy import arange
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# define derivative
def f(x, t, k):
    return -k*x

# create range of time values
t = arange(0.0, 3.0, 0.01)

# initial conditions and parameters
x0 = 1000.0
k = 0.8

# solve the differential equation
x = odeint(f, x0, t, args=(k,))

plt.plot(t, x)
plt.xlabel('time t')
plt.ylabel('Number')
plt.title('ODE Solution')
plt.show()
