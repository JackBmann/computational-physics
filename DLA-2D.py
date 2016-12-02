"""
DLA-2D.py
2D DLA
"""

from visual import *
from random import *
from visual.graph import *
from random import random
from vis import *

particles = []
fixed = []
grid = 100
maxquad = [0, 0, 0, 0, 0]
maxdist = max(maxquad)

scene.x = 400
scene.y = 0

num = int(raw_input("Numer of movements: "))

for i in arange(10000):
    particles.append(
        sphere(visible=0, pos=(int(random() * 2 * grid - grid / 2), int(random() * 2 * grid - grid / 2), 0)))

fixed.append(sphere(visible=1, pos=(0, 0, 0)))


def walk():
    global particles, maxdist, maxquad
    for i in particles:
        if i.x >= 0 and i.y >= 0 and i.pos.mag < maxquad[0] + 2:
            check(i, 0)
        elif i.x < 0 and i.y >= 0 and i.pos.mag < maxquad[1] + 2:
            check(i, 1)
        elif i.x < 0 and i.y < 0 and i.pos.mag < maxquad[2] + 2:
            check(i, 2)
        elif i.x >= 0 and i.y < 0 and i.pos.mag < maxquad[3] + 2:
            check(i, 3)
        elif i.pos < maxdist + 2:
            check(i, 4)
        else:
            i.pos = move(i)
            if i.x >= 0 and i.y >= 0 and i.pos.mag < maxquad[0] + 2:
                check(i, 0)
            elif i.x < 0 and i.y >= 0 and i.pos.mag < maxquad[1] + 2:
                check(i, 1)
            elif i.x < 0 and i.y < 0 and i.pos.mag < maxquad[2] + 2:
                check(i, 2)
            elif i.x >= 0 and i.y < 0 and i.pos.mag < maxquad[3] + 2:
                check(i, 3)
            elif i.pos < maxdist + 2:
                check(i, 4)
        maxdist = max(maxquad)


def move(point):
    global grid
    point.x += (random() * 3) - 1
    point.y += (random() * 3) - 1
    if (point.x > grid):
        point.x = grid - 1
    elif (point.x < -grid):
        point.x = -grid + 1
    if (point.y > grid):
        point.y = grid - 1
    elif (point.y < -grid):
        point.y = -grid + 1
    return point.pos


def check(point, maxtype):
    global fixed, particles, maxquad
    for j in fixed:
        if ((point.pos - j.pos).mag < 2):  # if the particle nears a fixed particle, it stops
            point.visible = 1
            fixed.append(point)
            particles.remove(point)
            if point.pos.mag > maxquad[maxtype]:
                maxquad[maxtype] = point.pos.mag
            break


colors = [color.red, color.blue, color.yellow, color.cyan, color.orange, color.green]


def fractDim():
    global fixed, grid, maxdist
    graph = gdisplay(x=400, y=450, width=400, height=400)
    dots = gdots(gdisplay=graph, color=color.red)
    eps1 = []
    eps = []
    N = []
    x1 = []
    y1 = []
    b = float(maxdist + 1)
    for i in range(6):
        eps1.append(b)
        b /= 2
    print len(eps1), " data points to be taken"
    x0 = [-maxdist - 1, -maxdist - 1, 0, 0]
    y0 = [-maxdist - 1, 0, 0, -maxdist - 1]
    for b in eps1:
        n = 0
        for i in arange(len(x0)):
            for k in fixed:
                if ((k.x > x0[i] - 1 and k.x < x0[i] + b + 1 and k.y > y0[i] and k.y < y0[i] + b) or
                        (k.x > x0[i] and k.x < x0[i] + b and k.y > y0[i] - 1 and k.y < y0[i] + b + 1) or (
                    (k.pos - vector(x0[i], y0[i], 0)).mag < 1) or
                        ((k.pos - vector(x0[i] + b, y0[i], 0)).mag < 1) or (
                    (k.pos - vector(x0[i] + b, y0[i] + b, 0)).mag < 1) or
                        ((k.pos - vector(x0[i], y0[i] + b, 0)).mag < 1)):
                    n += 1
                    curve(pos=[(x0[i], y0[i], 1), (x0[i] + b, y0[i], 1), (x0[i] + b, y0[i] + b, 1),
                               (x0[i], y0[i] + b, 1), (x0[i], y0[i], 1)], color=colors[eps1.index(b)])
                    x1.append(x0[i])
                    y1.append(y0[i])
                    x1.append(x0[i] + float(b) / 2)
                    y1.append(y0[i])
                    x1.append(x0[i] + float(b) / 2)
                    y1.append(y0[i] + float(b) / 2)
                    x1.append(x0[i])
                    y1.append(y0[i] + float(b) / 2)
                    break
        x0 = x1
        y0 = y1
        x1 = []
        y1 = []
        N.append(math.log10(n))
        eps.append(-math.log10(b))
        dots.plot(pos=(-math.log10(b), math.log10(n)))
    Sx = 0
    Sy = 0
    Sxy = 0
    Sx2 = 0
    Sy2 = 0
    n = len(eps)
    for i in arange(n):
        Sx += eps[i]
        Sx2 += eps[i] * eps[i]
        Sy += N[i]
        Sxy += eps[i] * N[i]
        Sy2 += N[i] * N[i]
    dim = float(n * Sxy - Sx * Sy) / (n * Sx2 - Sx * Sx)
    r = float(n * Sxy - Sx * Sy) / math.sqrt((n * Sx2 - Sx * Sx) * (n * Sy2 - Sy * Sy))
    print "fractal dimmension: ", dim
    print "R^2: ", r * r


i = 0
while i < num:
    i += 1
    print "movement ", i
    walk()
fractDim()
# for i in fixed:
#    i.visible=1
'''
DLA-2D.py
2D DLA
'''

from visual import *
from random import *
from visual.graph import *
from random import random

particles = []
fixed = []
grid = 100
maxquad = [0, 0, 0, 0, 0]
maxdist = max(maxquad)

scene.x = 400
scene.y = 0

num = int(raw_input("Numer of movements: "))

for i in arange(10000):
    particles.append(
        sphere(visible=0, pos=(int(random() * 2 * grid - grid / 2), int(random() * 2 * grid - grid / 2), 0)))

fixed.append(sphere(visible=1, pos=(0, 0, 0)))


def walk():
    global particles, maxdist, maxquad
    for i in particles:
        if i.x >= 0 and i.y >= 0 and i.pos.mag < maxquad[0] + 2:
            check(i, 0)
        elif i.x < 0 and i.y >= 0 and i.pos.mag < maxquad[1] + 2:
            check(i, 1)
        elif i.x < 0 and i.y < 0 and i.pos.mag < maxquad[2] + 2:
            check(i, 2)
        elif i.x >= 0 and i.y < 0 and i.pos.mag < maxquad[3] + 2:
            check(i, 3)
        elif i.pos < maxdist + 2:
            check(i, 4)
        else:
            i.pos = move(i)
            if i.x >= 0 and i.y >= 0 and i.pos.mag < maxquad[0] + 2:
                check(i, 0)
            elif i.x < 0 and i.y >= 0 and i.pos.mag < maxquad[1] + 2:
                check(i, 1)
            elif i.x < 0 and i.y < 0 and i.pos.mag < maxquad[2] + 2:
                check(i, 2)
            elif i.x >= 0 and i.y < 0 and i.pos.mag < maxquad[3] + 2:
                check(i, 3)
            elif i.pos < maxdist + 2:
                check(i, 4)
        maxdist = max(maxquad)


def move(point):
    global grid
    point.x += (random() * 3) - 1
    point.y += (random() * 3) - 1
    if (point.x > grid):
        point.x = grid - 1
    elif (point.x < -grid):
        point.x = -grid + 1
    if (point.y > grid):
        point.y = grid - 1
    elif (point.y < -grid):
        point.y = -grid + 1
    return point.pos


def check(point, maxtype):
    global fixed, particles, maxquad
    for j in fixed:
        if ((point.pos - j.pos).mag < 2):  # if the particle nears a fixed particle, it stops
            point.visible = 1
            fixed.append(point)
            particles.remove(point)
            if point.pos.mag > maxquad[maxtype]:
                maxquad[maxtype] = point.pos.mag
            break


colors = [color.red, color.blue, color.yellow, color.cyan, color.orange, color.green]


def fractDim():
    global fixed, grid, maxdist
    graph = gdisplay(x=400, y=450, width=400, height=400)
    dots = gdots(gdisplay=graph, color=color.red)
    eps1 = []
    eps = []
    N = []
    x1 = []
    y1 = []
    b = float(maxdist + 1)
    for i in range(6):
        eps1.append(b)
        b /= 2
    print len(eps1), " data points to be taken"
    x0 = [-maxdist - 1, -maxdist - 1, 0, 0]
    y0 = [-maxdist - 1, 0, 0, -maxdist - 1]
    for b in eps1:
        n = 0
        for i in arange(len(x0)):
            for k in fixed:
                if ((k.x > x0[i] - 1 and k.x < x0[i] + b + 1 and k.y > y0[i] and k.y < y0[i] + b) or
                        (k.x > x0[i] and k.x < x0[i] + b and k.y > y0[i] - 1 and k.y < y0[i] + b + 1) or (
                    (k.pos - vector(x0[i], y0[i], 0)).mag < 1) or
                        ((k.pos - vector(x0[i] + b, y0[i], 0)).mag < 1) or (
                    (k.pos - vector(x0[i] + b, y0[i] + b, 0)).mag < 1) or
                        ((k.pos - vector(x0[i], y0[i] + b, 0)).mag < 1)):
                    n += 1
                    curve(pos=[(x0[i], y0[i], 1), (x0[i] + b, y0[i], 1), (x0[i] + b, y0[i] + b, 1),
                               (x0[i], y0[i] + b, 1), (x0[i], y0[i], 1)], color=colors[eps1.index(b)])
                    x1.append(x0[i])
                    y1.append(y0[i])
                    x1.append(x0[i] + float(b) / 2)
                    y1.append(y0[i])
                    x1.append(x0[i] + float(b) / 2)
                    y1.append(y0[i] + float(b) / 2)
                    x1.append(x0[i])
                    y1.append(y0[i] + float(b) / 2)
                    break
        x0 = x1
        y0 = y1
        x1 = []
        y1 = []
        N.append(math.log10(n))
        eps.append(-math.log10(b))
        dots.plot(pos=(-math.log10(b), math.log10(n)))
    Sx = 0
    Sy = 0
    Sxy = 0
    Sx2 = 0
    Sy2 = 0
    n = len(eps)
    for i in arange(n):
        Sx += eps[i]
        Sx2 += eps[i] * eps[i]
        Sy += N[i]
        Sxy += eps[i] * N[i]
        Sy2 += N[i] * N[i]
    dim = float(n * Sxy - Sx * Sy) / (n * Sx2 - Sx * Sx)
    r = float(n * Sxy - Sx * Sy) / math.sqrt((n * Sx2 - Sx * Sx) * (n * Sy2 - Sy * Sy))
    print "fractal dimmension: ", dim
    print "R^2: ", r * r


i = 0
while i < num:
    i += 1
    print "movement ", i
    walk()
fractDim()
# for i in fixed:
#    i.visible=1
