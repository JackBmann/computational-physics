'''
sunspots.py
stores the data from sunspots.txt as a 2D list, prints it, then plots it
9/1/16
'''
import matplotlib.pyplot as plt
from numpy import loadtxt, floor, ceil, arange, min, max

f = open('sunspots.txt', 'r')
data = []
for eachLine in f.readlines():
    line = []
    for l in eachLine.strip().split():
        line.append(l)
    data.append(line)
print data

#read in file
data = loadtxt("sunspots.txt", float)
x = data[:, 0]
x = x/10.0
y = data[:, 1]

plt.scatter(x, y)
plt.xlabel("Year since First Observation")
plt.ylabel("Number of Sunspots")
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.show()

width = 5
histmin = floor(min(y))
histmax = ceil(max(y)) + width
ourbins = arange(histmin, histmax, width)
plt.hist(y, bins=ourbins)
plt.show()
