"""
nlmapwithsliders.py
implements widgets for plotting the nonlinear map
11/8/16
"""
from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

# set up plotting
ax = subplot(111)
subplots_adjust(left=0.25, bottom=0.25)

# values plotted
t = arange(0.0, 1.0, 0.01)
tcount = len(t)
xs = empty((tcount,))
xs[0] = 0.55
r0 = 0.25
r = 0.25

# calculate values for the initial plotting
for i in range(0, tcount-1):
    xs[i+1] = 4.0*r*xs[i]*(1.0 - xs[i])

p, = plot(t, xs, lw=2, color='red')
axis([0, 1, 0, 1])

axcolor = 'lightgoldenrodyellow'
axr = axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
axx = axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

# create sliders
sr = Slider(axr, 'r', 0.1, 1.0, valinit=r0)
sx = Slider(axx, 'x0', 0.1, 1.0, valinit=xs[0])


# define what to do upon updating
def update(val):
    x = sx.val
    r = sr.val
    xs[0] = x
    for i in range(0, tcount-1):
        xs[i+1] = 4.0*r*xs[i]*(1.0 - xs[i])
    p.set_ydata(xs)
    draw()

sr.on_changed(update)
sx.on_changed(update)

# reset button
resetax = axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sr.reset()
    sx.reset()

button.on_clicked(reset)

# choose colors
rax = axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'green', 'blue'), active=0)


def option(choice):
    p.set_color(choice)
    draw()

radio.on_clicked(option)
show()
