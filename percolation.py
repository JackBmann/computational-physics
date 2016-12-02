"""
percolation.py
simulation of percolation
"""
from visual import *
from visual.graph import *
from random import *
from vis import *

npoint = 80  # size of the surface
prob = float(raw_input("Enter occupation probability (0-1)"))
point = resize(array([0]), (npoint, npoint))

dis1 = display(x=600, width=400, height=400, xmin=0, xmax=npoint, ymin=0,
               ymax=npoint, center=(npoint / 2, npoint / 2, 0), title="Percolation")
# set up a random array
for i in range(1, npoint - 1):
    for j in range(1, npoint - 1):
        if random() < prob:
            point[i, j] = 1
            box(pos=(i, j, 0))

raw_input("Hit any key to see percolation")
ilabel = 1  # index of the cluster
for i in range(1, npoint - 1):
    for j in range(1, npoint - 1):
        if point[i, j] == 1:
            if point[i - 1, j] > 0 and point[i, j - 1] > 0:
                pointa = point[i - 1, j]
                pointb = point[i, j - 1]
                point[i, j] = pointa
                if pointa != pointb:  # a bridge between two clusters.  make them as one.
                    for m in arange(1, i + 1):
                        for n in arange(1, npoint - 1):
                            if point[m, n] == pointb:
                                point[m, n] = pointa

            elif point[i - 1, j] > 0:
                point[i, j] = point[i - 1, j]
            elif point[i, j - 1] > 0:
                point[i, j] = point[i, j - 1]
            else:
                ilabel = ilabel + 1
                point[i, j] = ilabel

# plot if any of the clusters percolates
colors = [(1, 1, 1), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 1, 1), (1, 1, 0)]  # set up 6 colors
icolor = 0
for i in range(1, ilabel + 1):
    iperco = zeros(4, int)  # array to record if a cluster connect at least two sides
    for j in range(1, npoint - 1):
        if point[1, j] == i: iperco[0] = 1
        if point[npoint - 2, j] == i: iperco[1] = 1
        if point[j, 1] == i: iperco[2] = 1
        if point[j, npoint - 2] == i: iperco[3] = 1
    if iperco[0] + iperco[1] + iperco[2] + iperco[3] >= 2:
        # print i, iperco
        icolor = icolor + 1
        for k in range(1, npoint - 1):
            for j in range(1, npoint - 1):
                if point[k, j] == i:
                    box(pos=(k, j, 0), color=colors[icolor % 6])


