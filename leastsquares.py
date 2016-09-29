'''
leastsquares.py
calculate the least squares fit of a straight line for data points
'''
import matplotlib.pyplot as plt
from numpy import linspace

#get the number of data points
N = input("Enter the number of data points N: ")
#initialize sums to zero
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
x_max = 0 #initialize the value of x

#input values of x, y and perform sums
for i in range(0, N):
    print "For point %s" %i
    x, y = input("Enter x, y: ")
    if x > x_max:
        x_max = x
    plt.plot(x, y, "bx")
    sum_x += x
    sum_y += y
    sum_xx += x*x
    sum_xy += x*y

#calculate the coefficients A and B
A = (sum_xx*sum_y - sum_x*sum_xy)/(N*sum_xx - sum_x*sum_x)
B = (N*sum_xy - sum_x*sum_y)/(N*sum_xx - sum_x*sum_x)

print "The straight line best fit is y = {0:5.2f} + {1:5.2f}x".format(A, B)

x_calc = linspace(0, x_max, 20)
y_calc = A + B*x_calc
plt.plot(x_calc, y_calc, "r+")
plt.show()
