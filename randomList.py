'''
randomList.py
creates a list of 100 random numbers and write them to a file
and create chi square value
'''
from numpy import random, ceil, floor, insert, zeros, savetxt, loadtxt, mean
from scipy.stats import itemfreq, chisquare

numbers = zeros((100, 2), int)
for i in range(0, 100):
    r = 10.0*random.random()
    r = int(floor(r))
    numbers[i, 0] = i
    numbers[i, 1] = r
print numbers
savetxt("random.txt", numbers, fmt="%i")

#load random numbers
data = loadtxt("random.txt")
#find observed numbers of randoms in each bin
O = itemfreq(data[:, 1])
print O
print "Mean value is ", mean(O), "\n"
#define intitial value of our sum
summed = 0
E = 10
#loop to perform calculation of chisquare
for i in range(0, 10):
    O_minus_E = O[i, 1] - E
    summed += O_minus_E**2/E
print "Our value of chi square is ", summed
print "numpy of chi square is ", chisquare(O)
