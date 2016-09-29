'''
coldmedicine.py
solves the differential equations for the amount of cold medicine
in the GI tract and bloodstream using Heun's method
9/27/16
'''
import matplotlib.pyplot as plt

#Parameters
tstop = 48 #time will be in hours
h = 0.01 #time step
k1 = 0.6931 #dissolving constant
k2 = 0.231 #clearing constant

#Initial values
t = 0
I = 0
x = 0 #no medication in GI tract initially
y = 0 #no medication  in bloodstream
tend = 0 #for Heun's method
xend = 0
yend = 0

#Define rates
def Rx(x, I):   #calculates the rate of absorption in GI tract
    return I - k1*x

def Ry(x, y):   #calculates the net rate out of the bloodstream
    return k1*x - k2*y

#Set up plot
plt.axis([0, tstop, 0, 12])

#Implement Heun's method
while t <= tstop:
    if t%6 <= 6.5%6:
        I = 20
    else:
        I = 0
    #use Heun's method
    xend = x + Rx(x, I)*h
    tend = t + h    #we don't really use this here
    yend = y + Ry(x, y)*h

    y += (Ry(x, y) + Ry(xend, yend))/2.0*h
    x += (Rx(x, I) + Rx(xend, I))/2.0*h

    plt.plot(t, x, 'b+')
    plt.plot(t, y, 'r+')
    t += h

plt.show()
