"""
bifurcationplot.py
11/8/16
"""
import matplotlib.pyplot as plt
from numpy import arange

r = arange(0.25, 1.0, 0.001)
xp = []
rp = []
for i in r:
    x = 0.55
    for j in range(200):
        x = 4*i*x*(1.0 - x)
        if j > 100:
            xp.append(x)
            rp.append(i)

plt.plot(rp, xp, 'ro')
plt.xlabel('r')
plt.ylabel('xn')
plt.show()
