"""
FinalProject.py
My final project analyzing the stock market with Chaos Theory
11/28/16
"""
from math import sqrt, log, sin
import matplotlib.pyplot as plt


def x(tau):
    rv = 0
    for i in range(1, tau+1):
        rv += xs[i]
    return 1.0/tau * rv


def X(t, tau):
    rvs = []
    for t in range(t, tau+1):
        rv = 0
        for i in range(1, t+1):
            rv += xs[i] - x(tau)
        rvs.append(1.0/tau * rv)
    return rvs
    # rv = 0
    # for i in range(1, t+1):
    #     rv += xs[i] - x(tau)
    # return 1.0/tau * rv


def S(tau):
    rv = 0
    for i in range(1, tau+1):
        rv += (xs[i] - x(tau))**2
    return sqrt(1/tau * rv)


def R(tau):
    t = 1   # 1 <= t <= tau
    return max(X(t, tau)) - min(X(t, tau))


def H(tau):
    c = 1.0     # constant that influences the value of H, default 1.0
    return log(R(tau)/(S(tau)*c))/log(tau)


def L(t):
    rv = 0
    for i in range(0, t+1):
        rv += log(xs[i+1]/xs[i], 2)
    return 1.0/t * rv

t = 1.0
tau = 2
xs = []
Hs = []
Ls = []
ts = []

while t < tau:
    xs.append(sin(t))
    Hs.append(H(tau))
    Ls.append(L(tau))
    ts.append(t)
    t += 0.1

predictability = 1.0/L(t)
plt.plot(xs, ts, 'k-')
plt.plot(Hs, ts, 'b-')
plt.plot(Ls, ts, 'r-')
