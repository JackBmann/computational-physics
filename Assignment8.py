"""
Completes Assignment 7
11/15/2016
"""
from __future__ import division
from visual import *
from vis import *
from random import random
from visual.graph import *

# Problem 1
print "Problem 1"
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
    func.plot(pos=(i, P[i + N]))

# Problem 2
print "\nProblem 2"
scene = display(x=300, y=0, width=800, height=800)
no_walkers = 200
walker_radius = 1.0
step = 1
avg_distance = 0
distance_squared = 0
t = 0
graph1 = gdisplay(x=0, y=0, width=300, height=200, title='Average Distance vs. Time')
graph2 = gdisplay(x=0, y=200, width=300, height=200, title='Theoretical Distance vs. Time')
graph3 = gdisplay(x=0, y=400, width=300, height=200, title='Diffusion vs. Time')
plot1 = gcurve(gdisplay=graph1, color=color.white)
plot2 = gcurve(gdisplay=graph2, color=color.yellow)
plot3 = gcurve(gdisplay=graph3, color=color.blue)
walker_list = []
for i in range(no_walkers):
    hue = (random(), random(), random())
    walker = sphere(radius=walker_radius, color=hue)
    walker.pos = vector(0, 0, 0)
    walker_list.append(walker)
    walker_list[i].trail = curve(pos=walker_list[i].pos, color=hue, radius=0.1)
def move():
    for i in range(no_walkers):
        r = random()
        if r <= 1/4:
            walker_list[i].pos.x += step
        elif r <= 1/2:
            walker_list[i].pos.x -= step
        elif r <= 3/4:
            walker_list[i].pos.y += step
        else:
            walker_list[i].pos.y -= step
        walker_list[i].trail.append(pos=walker_list[i].pos)
while t < 500:
    for i in range(no_walkers):
        avg_distance += mag(walker_list[i].pos)
        distance_squared += mag(walker_list[i].pos)**2
    avg_distance /= no_walkers
    distance_squared /= no_walkers
    t += 1
    diffusion = (distance_squared - avg_distance**2) / (4*t)
    plot1.plot(pos=(t, avg_distance))
    plot2.plot(pos=(t, sqrt(t)))
    plot3.plot(pos=(t, diffusion))
    move()
    rate(300)

# Problem 3
print "\nProblem 3"
npoint = 4
prob = float(raw_input("Enter occupation probability (0-1)"))
point = resize(array([0]), (npoint, npoint))
dis1 = display(x=600, width=400, height=400, xmin=0, xmax=npoint, ymin=0,
               ymax=npoint, center=(npoint / 2, npoint / 2, 0), title="Percolation")
for i in range(1, npoint - 1):
    for j in range(1, npoint - 1):
        if random() < prob:
            point[i, j] = 1
            box(pos=(i, j, 0))
raw_input("Hit any key to see percolation")
ilabel = 1
for i in range(1, npoint - 1):
    for j in range(1, npoint - 1):
        if point[i, j] == 1:
            if point[i - 1, j] > 0 and point[i, j - 1] > 0:
                pointa = point[i - 1, j]
                pointb = point[i, j - 1]
                point[i, j] = pointa
                if pointa != pointb:
                    for m in arange(1, i + 1):
                        for n in arange(1, npoint - 1):
                            if point[m, n] == pointb:
                                point[m, n] = pointa
            elif point[i - 1, j] > 0:
                point[i, j] = point[i - 1, j]
            elif point[i, j - 1] > 0:
                point[i, j] = point[i, j - 1]
            else:
                ilabel += 1
                point[i, j] = ilabel
colors = [(1, 1, 1), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 1, 0)]  # set up 6 colors
icolor = 0
for i in range(1, ilabel + 1):
    iperco = zeros(4, int)
    for j in range(1, npoint - 1):
        if point[1, j] == i:
            iperco[0] = 1
        if point[npoint - 2, j] == i:
            iperco[1] = 1
        if point[j, 1] == i:
            iperco[2] = 1
        if point[j, npoint - 2] == i:
            iperco[3] = 1
    if iperco[0] + iperco[1] + iperco[2] + iperco[3] >= 2:
        icolor += 1
        for k in range(1, npoint - 1):
            for j in range(1, npoint - 1):
                if point[k, j] == i:
                    box(pos=(k, j, 0), color=colors[icolor % 6])

# Problem 4
print "Problem 4"
npoint = 16     # 32
prob = float(raw_input("Enter occupation probability (0-1)"))
point = resize(array([0]), (npoint, npoint))
dis1 = display(x=600, width=400, height=400, xmin=0, xmax=npoint, ymin=0,
               ymax=npoint, center=(npoint / 2, npoint / 2, 0), title="Percolation")
for i in range(1, npoint - 1):
    for j in range(1, npoint - 1):
        if random() < prob:
            point[i, j] = 1
            box(pos=(i, j, 0))
raw_input("Hit any key to see percolation")
ilabel = 1
for i in range(1, npoint - 1):
    for j in range(1, npoint - 1):
        if point[i, j] == 1:
            if point[i - 1, j] > 0 and point[i, j - 1] > 0:
                pointa = point[i - 1, j]
                pointb = point[i, j - 1]
                point[i, j] = pointa
                if pointa != pointb:
                    for m in arange(1, i + 1):
                        for n in arange(1, npoint - 1):
                            if point[m, n] == pointb:
                                point[m, n] = pointa
            elif point[i - 1, j] > 0:
                point[i, j] = point[i - 1, j]
            elif point[i, j - 1] > 0:
                point[i, j] = point[i, j - 1]
            else:
                ilabel += 1
                point[i, j] = ilabel
colors = [(1, 1, 1), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 1, 0)]  # set up 6 colors
icolor = 0
for i in range(1, ilabel + 1):
    iperco = zeros(4, int)
    for j in range(1, npoint - 1):
        if point[1, j] == i:
            iperco[0] = 1
        if point[npoint - 2, j] == i:
            iperco[1] = 1
        if point[j, 1] == i:
            iperco[2] = 1
        if point[j, npoint - 2] == i:
            iperco[3] = 1
    if iperco[0] + iperco[1] + iperco[2] + iperco[3] >= 2:
        icolor += 1
        for k in range(1, npoint - 1):
            for j in range(1, npoint - 1):
                if point[k, j] == i:
                    box(pos=(k, j, 0), color=colors[icolor % 6])
