"""
bouncing.py
use VPython to animate ball bouncing in a box
9/29/16
"""
from visual import *
from random import uniform

# create walls, floor, and ceiling
side = 4.0
thickness = 0.3

wallRight = box(pos=vector(side, 0, 0), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))
wallRight.velocity = vector(-0.1, 0, 0)
wallLeft = box(pos=vector(-side, 0, 0), length=thickness, height=2*side, width=2*side, color=color.gray(0.7))
wallLeft.velocity = vector(0.1, 0, 0)
wallBack = box(pos=vector(0, 0, -side), length=2*side, height=2*side, width=2*thickness, color=color.gray(0.7))
floor = box(pos=vector(0, -side, 0), length=2*side, height=thickness, width=2*side, color=color.gray(0.7))
ceiling = box(pos=vector(0, side, 0), length=2*side, height=thickness, width=2*side, color=color.gray(0.7))

# create balls
number = 25
ball_radius = 0.2
max_pos = side - 0.5*thickness - ball_radius
max_vel = 50.0

ball_list = []
for i in range(number):
    ball = sphere(color=color.green, raduis=ball_radius)
    ball.pos = max_pos*vector(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
    ball.velocity = max_vel*vector(uniform(-1, 1), uniform(-1, 1), uniform(-1, 1))
    ball.trail = curve(pos=[ball.pos], color=ball.color)
    ball_list.append(ball)

# animate the balls
h = 0.001   # time step
win = 500   # height and width of the display
scene = display(title="Bouncing Balls", width=win, height=win, x=0, y=0, center=(side, side, side))

while True:
    rate(100)   # set the refresh rate for the animation (times per second)
    for ball in ball_list:
        # move the balls
        ball.pos += ball.velocity*h # + 1.0/2.0*vector(0, -9.8, 0)*h**2
        # ball.velocity += vector(0, -9.8, 0)*h
        ball.trail.append(pos=ball.pos, retain=50)
        # make them bounce
        if ball.pos.x > wallRight.pos.x:
            ball.velocity.x = -ball.velocity.x + wallRight.velocity.x   # reflect at right wall
            ball.pos.x += -0.5*thickness - ball.radius

        if ball.pos.x < wallLeft.pos.x:
            ball.velocity.x = -ball.velocity.x + wallLeft.velocity.x    # reflect at left wall
            ball.pos.x += 0.5*thickness + ball.radius

        if ball.pos.y > ceiling.pos.y:
            ball.velocity.y = -ball.velocity.y  # reflect at ceiling
            ball.pos.y += -0.5*thickness - ball.radius

        if ball.pos.y < floor.pos.y:
            ball.velocity.y = -ball.velocity.y  # reflect at floor
            ball.pos.y += 0.5*thickness + ball.radius

        if ball.pos.z < wallBack.pos.z:
            ball.velocity.z = -ball.velocity.z  # reflect at back wall
            ball.pos.z += 0.5*thickness + ball.radius

        if ball.pos.z > max_pos:
            ball.velocity.z = -ball.velocity.z  # reflect at front wall
            ball.pos.z += -0.5*thickness - ball.radius

        if wallRight.pos.x - wallLeft.pos.x < 2*ball.radius + 0.5*thickness:
            wallRight.velocity.x = 0
            wallLeft.velocity.x = 0

        wallRight.pos += wallRight.velocity*h
        wallLeft.pos += wallLeft.velocity*h
