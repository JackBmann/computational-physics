"""
fern.py
"""
from visual import *
from vis import *
from random import *

rad = 0.05

scene = display(height=600, width=600, x=0, y=300)

plotNew = vector(0, 0, 0)
plotOld = vector(0, 0, 0)

plotOld.x = 0
plotOld.y = 0

p = 0.849
q = 0.0371

scene.center = (0, 5, 0)

new_point = sphere(pos=(plotOld.x, plotOld.y, 0), radius=0, visible=0)

for i in range(0, 10000):
    prob = random()

    if prob <= 0.043:
        plotNew.x = 0
        plotNew.y = 0.16 * plotOld.y

    if prob > 0.043 and prob <= 0.833:
        plotNew.x = p * plotOld.x + q * plotOld.y
        plotNew.y = -q * plotOld.x + p * plotOld.y + 1.6

    if prob > 0.833 and prob <= 0.919:
        plotNew.x = 0.197 * plotOld.x - 0.226 * plotOld.y
        plotNew.y = 0.226 * plotOld.x + 0.197 * plotOld.y + 1.6

    if prob > 0.919:
        plotNew.x = -0.15 * plotOld.x + 0.283 * plotOld.y
        plotNew.y = 0.260 * plotOld.x + 0.238 * plotOld.y + 0.44

    new_point.color = color.yellow
    new_point.radius = rad
    new_point = sphere(pos=(plotNew.x, plotNew.y, 0), radius=5 * rad, color=color.red)
    plotOld.x = plotNew.x
    plotOld.y = plotNew.y
