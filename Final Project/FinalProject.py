"""
FinalProject.py
Jack Baumann's final project analyzing the stock market with Chaos Theory
11/28/16
"""
from math import sqrt, log, sin, pi
import matplotlib.pyplot as plt
from numpy import loadtxt


def data(x):
    return prices[x-1]
    # return (sin(5.5*pi*x/100.0 + 5.5) + 1.0)/2.0
    # return (sin(x) + 1.0)/2.0


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
    # 1 <= t <= tau
    return max(X(t, tau)) - min(X(t, tau))


def H(tau):
    c = 1.0     # constant that influences the value of H, default 1.0
    if R(tau) == 0:
        return 0
    return log(R(tau)/(S(tau)*c))/log(tau)


def L(t):
    sum = 0
    i = 1
    while i <= t:
        if data(i) != 0 and data(i+h)/data(i) != 0:
            sum += log(data(i+h)/data(i), 2)
        i += h
    return 1.0/t * sum


def avg(vals):
    return sum(vals)/len(vals)


t = 1
tau = 25
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
    Lt = L(t)
    Ls.append(Lt)
    ps.append(1.0/Lt)
    t += h

sub = "Hurst Exponent: {0:f}, Lyapunov Exponent: {1:f}, Predictability (day): {2:f}".format(avg(Hs), avg(Ls), avg(ps))
print sub
plt.figure(1)
plt.subplot(411)
plt.title(sub, fontsize=10)
plt.suptitle('Apple Stock Price Over 25 Days', y=0.97, fontsize=18)
plt.plot(ts, xs, 'k-', label='Stock Price')
plt.legend(loc='best')

plt.subplot(412)
plt.plot(ts, Hs, 'r-', label='Hurst Exponent')
plt.legend(loc='best')

plt.subplot(413)
plt.plot(ts, Ls, 'b-', label='Lyapunov Exponent')
plt.legend(loc='best')

plt.subplot(414)
plt.plot(ts, ps, 'g-', label='Predictability')
plt.legend(loc='best')
plt.xlabel('Time t (Days)')
plt.show()
