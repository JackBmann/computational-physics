'''
standardDeviation.py
calculates average and standard deviation for a dataset
9/8/16
'''
from math import sqrt

#dataset
data = [12.5, 11.2, 13.8, 10.9, 11.2, 11.6, 12.1]

#find the average value
def mean(data):
    #initialize sum
    sum_x = 0
    #add up values
    for x in data:
        sum_x += x
    #divide b N to get average
    N = len(data)
    return sum_x/N

#calculate the standard deviation
def rms(data):
    #get average value
    x_bar = mean(data)
    #initialize sum of squares
    sum_squares = 0.0
    #loop over sum
    for x in data:
        sum_squares += (x - x_bar)**2
    return sqrt(sum_squares/len(data))

print "Average and standard deviation are {0:5.2f} and {1:5.2f}".format(mean(data), rms(data))