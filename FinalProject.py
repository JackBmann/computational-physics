"""
FinalProject.py
My final project analyzing the stock market with Chaos Theory
11/28/16
"""
from math import sqrt, log, sin, pi
import matplotlib.pyplot as plt
from numpy import loadtxt


def data(x):
    return prices[x-1]
    # return (sin(2*pi*x/3) + 1)/2


def x(tau):
    sum = 0
    i = 1
    while i <= tau:
        sum += data(i)
        i += h
    return 1.0/tau * sum


def X(t, tau):
    rvs = []
    # t = 0
    while t <= tau:
        sum = 0
        i = 1
        while i <= t:
            sum += data(i) - x(tau)
            i += h
        rvs.append(sum)
        t += h
    return rvs


def S(tau):
    sum = 0
    i = 1
    while i <= tau:
        sum += (data(i) - x(tau)) ** 2
        i += h
    return sqrt(1.0/tau * sum)


def R(tau):
    # t = tau/2   # 1 <= t <= tau
    return max(X(t, tau)) - min(X(t, tau))


def H(tau):
    c = 1.0     # constant that influences the value of H, default 1.0
    if R(tau) == 0:
        return 0
    return log(R(tau)/(S(tau)*c))/log(tau)


def L(t):
    rv = 0
    i = 1
    while i <= t:
        if data(i) > 0 and data(i+h)/data(i) > 0:
            rv += log(data(i+h)/data(i), 2)
        i += h
    return 1.0/t * rv

t = 1
tau = 250
h = 1
xs = []
ts = []
Hs = []
Ls = []
ps = []
prices = loadtxt("Final Project Apple Stock Prices.csv", skiprows=1, delimiter=',')[:, 4]

while t <= tau:
    xs.append(data(t))
    ts.append(t)
    Hs.append(H(tau))
    Ls.append(L(t))
    # ps.append(1.0/L(t))
    t += h

print ts
print xs
print Hs
print Ls
print ps
# predictability = 1.0/L(t)
plt.plot(ts, xs, 'k-', label='Stock Price')
plt.plot(ts, Hs, 'r-', label='Hurst Exponent')
plt.plot(ts, Ls, 'b-', label='Lyapunov Exponent')
# plt.plot(ts, ps, 'g-', label='Predictability')
plt.legend(loc='best')
plt.show()
