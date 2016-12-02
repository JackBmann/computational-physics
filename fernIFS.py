"""
fernIFS.py
Interated Function Set Fern Fractal
"""
from visual import*
from visual.graph import*
from vis import *
from random import*

rad = 5e-3  # radius of a point

scene = display(title="IFS Fern", height=600, width=600, x=0, y=0,
                center=vector(0,5,0), range=(6,6,6))

x = 0.0
y = 0.0
xold = 0
yold = 0

a = [0.0, 0.849,  0.197, -0.15]
b = [0.0, 0.0371, -0.226,  0.283]
c = [0.0, -0.0371, 0.226,  0.260]
d = [0.16, 0.849, 0.197,  0.238]
e = [0.0,  0.0,   0.0,    0.0]
f = [0.0,  1.6,   1.6,    0.44]

k = 5

new_point=sphere(pos=(x,y), radius=0, visible=0)

while 1:
    # rate(1500)
    # num = randint(0,k-1)
    prob = random()
    if prob <= 0.043:
        num = 0
    if prob > 0.043 and prob <=0.833:
        num = 1
    if prob > 0.833 and prob <=0.919:
        num = 2
    if prob > 0.919:
        num = 3

    x = a[num]*xold + b[num]*yold + e[num]
    y = c[num]*xold + d[num]*yold + f[num]

    new_point.color=color.green
    new_point.radius=rad
    new_point=sphere(pos=(x,y), radius=5.0*rad, color=color.red)
    xold = x
    yold = y
