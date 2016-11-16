"""
Completes Assignment 7
11/15/2016
"""
from __future__ import division
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons
from visual import *
from visual.graph import *
from math import *

# # Problem 1
# print "Problem 1"
# ax = subplot(111)
# subplots_adjust(bottom=0.25)
# t = arange(0.0, 1.0, 0.01)
# tcount = len(t)
# xs = empty((tcount,))
# xs[0] = 0.55
# r0 = 0.892
# r = r0
# for i in range(0, tcount-1):
#     xs[i+1] = 4.0*r*xs[i]*(1.0 - xs[i])
# p, = plot(t, xs, lw=2, color='red')
# axis([0, 1, 0, 1])
# axr = axes([0.15, 0.1, 0.65, 0.03], axisbg='lightgoldenrodyellow')
# sr = Slider(axr, 'r', 0.1, 1.0, valinit=r0)
# def update(val):
#     r = sr.val
#     xs[0] = 0.55
#     for i in range(0, tcount-1):
#         xs[i+1] = 4.0*r*xs[i]*(1.0 - xs[i])
#     p.set_ydata(xs)
#     draw()
# sr.on_changed(update)
# print "When r = 0.26, the function is 1/x, when r = 0.826 the function has 2 equilibrium points, and when" \
#       " r = 0.892 the function has 4 equalibrium points."
# show()
#
# # Problem 2 part a
# print "\nProblem 2 part a"
# c = gdots(color=color.red)
# for r in arange(0, 1, 0.005):
#     x = 0.25
#     for i in range(900):
#         x = 4*r*x*(1-x)
#         if i > 800:
#             c.plot(pos=(r, x))
#
# # Problem 2 part b
# print "\nProblem 2 part b"
# graph = gdisplay(x=0, y=0, width=1200, height=1000, title='Lyapunov exponent', xtitle='r', ytitle='lambda',
#                  xmin=0, xmax=1, ymin=-1.5, ymax=1.5)
# graph1 = gdots(color=color.yellow)
# N = 1000
# for r in arange(0.01, 1.0, 0.001):
#     x = 0.55
#     lamb = 0
#     sumx = 0
#     for i in range(0, N):
#         dx = 4*r*(1-2*x)
#         if i > N/2:
#             sumx += log(abs(dx))
#         x = 4*r*x*(1-x)
#     lamb = sumx/log(2)/N
#     graph1.plot(pos=(r, lamb))

# Problem 3
print "\nProblem 3"
r = arange(0.25, 1.0, 0.001)
xp = []
rp = []
for i in r:
    x = 0.55
    for j in range(200):
        x = 4*i*x*(1.0 - x)
        if 0.0 < x < 0.5:
            x = 2*r*x
            if j > 100:
                xp.append(x)
                rp.append(i)
        elif 0.5 < x < 1:
            x = 2*r*(1.0 - x)
            if j > 100:
                xp.append(x)
                rp.append(i)
plt.plot(rp, xp, 'ro')
plt.xlabel('r')
plt.ylabel('xn')
plt.show()

# # Problem 6
# print "\nProblem 6"
# plot2 = gdisplay(x=0, y=401, background=color.white, foreground=color.black, height=400, width=400,
#                  title='Poincare  Map', xtitle='y', ytitle='vy')
# funct2 = gdots(color=color.blue)
# dt = 0.01
# Es = [0.05, 0.13, 0.14]
# x = Es[0]
# y = 0.0
# vx = 0
# vy = 0.215
# t = 0
# def ax(x, y): return -x-2*x*y
# def ay(x, y): return -y-x**2 + y**2
# while t < 5000:
#     k1vx = ax(x, y)*dt
#     k1x = vx*dt
#     k1vy = ay(x, y)*dt
#     k1y = vy*dt
#     k2vx = ax(x+k1x/2, y+k1y/2)*dt
#     k2x = (vx + k1vx/2)*dt
#     k2vy = ay(x+k1x/2, y+k1y/2)*dt
#     k2y = (vy + k1vy/2)*dt
#     k3vx = ax(x + k2x/2, y+k2y/2)*dt
#     k3x = (vx + k2vx/2)*dt
#     k3vy = ay(x + k2x/2, y+k2y/2)*dt
#     k3y = (vy + k2vy/2)*dt
#     k4vx = ax(x+k3x, y+k3y)*dt
#     k4x = (vx + k3vx)*dt
#     k4vy = ay(x+k3x, y+k3y)*dt
#     k4y = (vy + k3vy)*dt
#     vx += (k1vx+2*k2vx+2*k3vx+k4vx)/6
#     x += (k1x+2*k2x+2*k3x+k4x)/6
#     vy += (k1vy+2*k2vy+2*k3vy+k4vy)/6
#     y += (k1y+2*k2y+2*k3y+k4y)/6
#     if -0.001 < x < 0.001:
#         funct2.plot(pos=(y, vy))
#     t += dt
