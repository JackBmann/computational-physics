'''
simpleplot.py
plots some functions
9/1/16
'''
import numpy as np  #import specialized functions
import matplotlib.pyplot as plt    #import plotting routines

n = 200 #number of points in our plot

x = np.linspace(-5, 5, n)    #creates 100 points from -5 to 5
y = 100*np.exp(-x*x)        #creates a list of function values
y2 = 100*np.exp(-np.fabs(x))
plt.xlim(-5, 5)     #sets the x-axis values from -5 to 5
plt.ylim(0, 120)    #sets the y-axis range plotted from 0 to 120
plt.plot(x,y,'yD',label='squared')
plt.plot(x,y2,'cs',label='absolute')
plt.legend(loc='upper left')
plt.savefig("plot1.png")
plt.show()

#create a list of independant variables
t = np.linspace(-5.0, 5.0, 1000)

plt.figure(1)   #create a figure
plt.subplot(311)    #create an upper subplot of the figure
plt.ylabel("Time t")
plt.xlabel("Transform")
plt.plot(t, np.exp(-t*t)*np.sin(2*np.pi*t), 'k+')   #plot upper curve

plt.subplot(312)    #create lower subplot
plt.ylabel("Time t")
plt.xlabel("Signal")
plt.plot(t, np.cos(2*np.pi*t), 'yx')    #plot lower curve

plt.subplot(313)    #create lower subplot
plt.ylabel("Time t")
plt.xlabel("Signal Squared")
plt.plot(t, np.cos(2*np.pi*t)**2, 'm-')    #plot lower curve

plt.show()