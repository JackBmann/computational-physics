"""
randomwalk1D.py
Monte Carlo simulation of a random walk in 1-D
"""
from __future__ import division
from visual import *
from visual.graph import *
from random import random

n_trial = 1000
P = []
xsum = 0.0
x2sum = 0.0
x = 0

prob = input("Enter the probability to move to the right < 1 ")
N = input("Input the number of steps, N ")

plot = gdisplay(x=0, y=0, height=400, width=800, title='Random Walk', xtitle='x', ytitle='n', xmin=-N / 2, xmax=N / 2)
func = gvbars(delta=.75, color=color.green)
for i in arange(0, 2 * N):
    P.append(0)


def data(x):
    global xsum, x2sum, P
    xsum += x
    x2sum += x * x
    P[x + N] += 1


def average():
    global xsum, x2sum, P
    xbar = 0.
    x2bar = 0.
    variance = 0.
    norm = 1 / n_trial
    xbar = xsum * norm
    x2bar = x2sum * norm
    for i in range(0, 2 * N):
        P[i] *= 2 * norm
        if P[i] > 0:
            break
    variance = abs(x2bar - xbar * xbar)
    sigma = sqrt(variance)
    print "Mean Displacement = ", xbar
    print "Sigma = ", sigma


for k in range(0, n_trial):
    x = 0
    for i_step in range(0, N):
        if random() <= prob:
            x += 1
        else:
            x -= 1
    data(x)

average()
for i in range(-N, N, 1):
    func.plot(pos=(i, P[i + N]))  # vbars



