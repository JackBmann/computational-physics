'''
humanmotion.py
reads a datafile of time and position valuse, calculates velocity
and acceleration of points, writes points to a file, and graphs
9/20/16
'''
import numpy as np
import matplotlib.pyplot as plt

#get the filename containing the data from the user
#filename = raw_input("Enter datafile name ")
filename = "Foot.csv"

data = np.genfromtxt(filename, delimiter=',', filling_values=0.0, skip_header=1)

#slice array into data variables as columns
t = data[:, 0]
y = data[:, 1]

#get the number of data points
N = len(t)

#set up lists of calculated variables
vel = np.zeros(N, float)
accel = np.zeros(N, float)

#set up plots
plt.figure(1) #create a figure to hold plots
plt.figure(1).suptitle("Position Velocity Acceleration Graphs")

#calculate velocity and acceleration
for i in range(1, N):
    vel[i] = (y[i] - y[i-1])/(t[i] - t[i-1])

for i in range(2, N):
    accel[i] = (vel[i] - vel[i-1])/(t[i] - t[i-1])

#plot our results
plt.subplot(311)
plt.xlabel('time (s)')
plt.ylabel('position (cm)')
plt.plot(t, y)

plt.subplot(312)
plt.xlabel('time (s)')
plt.ylabel('velocity (cm/s)')
plt.plot(t, vel)

plt.subplot(313)
plt.xlabel('time (s)')
plt.ylabel('acceleration (cm/s/s)')
plt.plot(t, accel)

#write data to a file
#open our file
outfile = open('analysis.txt', 'w')

L = ['Time', 'Position', 'Velocity', 'Acceleration']
print '{0:10s}{1:10s}{2:10s}{3:10s}'.format(L[0], L[1], L[2], L[3])
print >> outfile, '{0:10s}{1:10s}{2:10s}{3:10s}'.format(L[0], L[1], L[2], L[3])

for i in range(len(accel)):
    print '{0:8.2f}{1:8.2f}{2:8.2f}{3:8.2f}'.format(t[i], y[i], vel[i], accel[i])
    print >> outfile, '{0:8.2f}{1:8.2f}{2:8.2f}{3:8.2f}'.format(t[i], y[i], vel[i], accel[i])

outfile.close()
plt.show()
