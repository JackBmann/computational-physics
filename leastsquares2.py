'''
leastsquares2.py
calculate the least squares fit of a straight line for data points
and plot the data with error bars as well as the straight line fit
'''
import matplotlib.pyplot as plt
from numpy import linspace, append, loadtxt, std

#initialize sums to zero
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
x_max = 0 #initialize the value of x

#read in the data and put it into an array
data = loadtxt("MagData.txt", skiprows=1)

#create 3 lists for data
x = data[:, 0]
y = data[:, 1]
err = data[:, 2]

#get length of data
N = len(x)

#input values of x, y and perform sums
for i in range(0, N):
    if x[i] > x_max:
        x_max = x[i]
    #plt.plot(x, y, "bx")
    sum_x += x[i]
    sum_y += y[i]
    sum_xx += x[i]*x[i]
    sum_xy += x[i]*y[i]

#calculate the coefficients A and B
A = (sum_xx*sum_y - sum_x*sum_xy)/(N*sum_xx - sum_x*sum_x)
B = (N*sum_xy - sum_x*sum_y)/(N*sum_xx - sum_x*sum_x)

print "The straight line best fit is y = {0:5.2f} + {1:5.2f}x".format(A, B)

plt.errorbar(x, y, yerr=std(y)/N, fmt="bx")

x_calc = linspace(0, x_max, 20)
y_calc = A + B*x_calc
plt.plot(x_calc, y_calc, "r-")
plt.show()
