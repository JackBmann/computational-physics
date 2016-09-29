"""
bouncing.py
use VPython to animate ball bouncing in a box
9/29/16
"""
from visual import *
from numpy import random, uniform

# create walls, floor, and ceiling
side = 4.0
thickness = 0.3

wallRight = box(pos=vector(side, 0, 0), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))
wallLeft = box(pos=vector(-side, 0, 0), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))
wallBack = box(pos=vector(0, 0, -side), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))
floor = box(pos=vector(0, -side, 0), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))
ceiling = box(pos=vector(0, side, 0), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))

# create balls
number = 25
ball_radius = 0.2

ball_list = []
for i in range(number):
    ball = sphere(color=color.green, raduis=ball_radius)
    ball.pos = 5.0*vector(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
    ball.velocity = 5.0*vector(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
    ball_list.append(ball)
