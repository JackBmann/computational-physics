"""
lyapunov.py
11/10/16
"""
from visual import *
from visual.graph import *
from math import log

# set up graphing
graph = gdisplay(x=0, y=0, width=1200, height=1000, title='Lyapunov exponent', xtitle='r', ytitle='lambda',
                 xmin=0, xmax=1, ymin=-1.5, ymax=1.5)
graph1 = gdots(color=color.yellow)

# number of iterations
N = 1000

# iterate over different values of r
for r in arange(0.01, 1.0, 0.001):
    x = 0.55    # seed value
    lamb = 0
    sumx = 0
    # iterate and remove transients
    for i in range(0, N):
        dx = 4*r*(1-2*x)
        if i > N/2:
            sumx += log(abs(dx))
        x = 4*r*x*(1-x)
    lamb = sumx/log(2)/N
    graph1.plot(pos=(r, lamb))
