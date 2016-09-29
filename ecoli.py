'''ecoli.py
simulate diffusion of a bacterium
See Physics Today Jan. 2000 article by Berg
'''

from visual import*
from random import*
scene.autoscale=1


# make a bacterium
# scale length in microns, time in seconds (real time)

ecoli = frame(axis=(0,1,0))
cylinder(frame=ecoli, pos=(-1,0,0), axis=(2,0,0), radius = 0.35)
sphere(frame=ecoli, pos=(1,0,0), radius = 0.35)
sphere(frame=ecoli, pos=(-1,0,0), radius = 0.35)
track = curve(color=color.green)
#ecoli.axis = vector(0,1,0)
ecoli.speed = 10

h = 0.01
omega = 25
deltaangle = 0.25
stepangle = sqrt(2*deltaangle*h)

t = 0
clock = label(pos=(0,0,0), text = "Time: "+ str(t), height = 12, opacity = 0.0, yoffset=-60, line = 0, color = color.cyan)

#create people to be infected
num_balls = 500
ball_radius = 1.5
ball_list = []


for i in range(num_balls):
    ball = sphere(color=color.blue, radius = ball_radius)
    ball.pos = vector(uniform(-20, 20), uniform(-20,20), uniform(-20,20))
    ball.velocity = vector(uniform(-4,4), uniform(-4,4), uniform(-4,4))
    ball_list.append(ball)

while true:
    rate(250)
    ecoli.pos += ecoli.axis*ecoli.speed*h
    ecoli.rotate(axis=ecoli.axis, angle=omega*h)
    if ecoli.axis.y < 0:
        track.append(pos=ecoli.pos, color = color.red )
    else:
        track.append(pos=ecoli.pos, color = color.yellow )
    rotaxis = cross(vector(1,0,0), ecoli.axis)
    rotaxis = norm(rotaxis)
    rotaxis = rotate(rotaxis, angle = 2.0*pi*random(), axis=ecoli.axis)
    clock.text = "Time: " + str(t)
    while len(clock.text) < 12:
        clock.text += "0"
    ecoli.rotate(angle=stepangle, axis = rotaxis)

    for ball in ball_list:
        ball.pos = ball.pos + ball.velocity*h
        if mag(ecoli.pos - ball.pos) <= 5:
            ball.color = color.green
                   
        
    t += h
    




              
