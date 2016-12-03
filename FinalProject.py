"""
FinalProject.py
My final project analyzing the stock market with Chaos Theory
11/28/16
"""
from math import sqrt, log, sin, pi
import matplotlib.pyplot as plt


def data(x):
    return sin(x)


def x(tau):
    rv = 0
    i = 1
    while i <= tau:
    # for i in range(1, tau+1):
    #     rv += xs[i]
        rv += data(i)
        i += h
    return 1.0/tau * rv


def X(t, tau):
    rvs = []
    while t <= tau:
    # for t in range(t, tau+1):
        rv = 0
        i = 1
        while i <= t:
        # for i in range(1, t+1):
            # rv += xs[i] - x(tau)
            rv += data(i) - x(tau)
            i += h
        rvs.append(1.0/tau * rv)
        t += h
    return rvs
    # rv = 0
    # for i in range(1, t+1):
    #     rv += xs[i] - x(tau)
    # return 1.0/tau * rv


def S(tau):
    rv = 0
    i = 1
    while i <= tau:
    # for i in range(1, tau+1):
    #     rv += (xs[i] - x(tau))**2
        rv += (data(i) - x(tau)) ** 2
        i += h
    return sqrt(1.0/tau * rv)


def R(tau):
    t = tau/2   # 1 <= t <= tau
    return max(X(t, tau)) - min(X(t, tau))


def H(tau):
    c = 1.0     # constant that influences the value of H, default 1.0
    return log(R(tau)/(S(tau)*c))/log(tau)


def L(t):
    rv = 0
    i = 0.1
    while i <= t:
    # for i in range(0, t):
        rv += log(abs(data(i+h)/data(i)), 2)
    #     rv += log(xs[i+1]/xs[i], 2)
        i += h
    return 1.0/t * rv

t = 0.1
tau = 2*pi
h = 0.1
xs = []
ts = []
Hs = []
Ls = []
ps = []

while t <= tau:
    xs.append(data(t))
    ts.append(t)
    Hs.append(H(tau))
    Ls.append(L(t))
    # ps.append(1.0/L(t))
    t += h

print len(xs), len(ts), len(Hs)
print ts
print xs
print Hs
print Ls
# predictability = 1.0/L(t)
plt.plot(ts, xs, 'k-')
plt.plot(ts, Hs, 'b-')
plt.plot(ts, Ls, 'r-')
plt.show()
