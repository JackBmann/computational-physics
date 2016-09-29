'''
derivative.py
calculates the derivative of a function by the 2pt and 3pt methods
9/15/16
'''
import matplotlib.pyplot as plt

#set our grid(mesh) size
h = 0.2
#initialize independent variable x
x = 0

def f(x):
    return x**3 - 2.0*x**2 - 5.0*x + 2.0

while x < 5.0:
    der2 = (f(x+h) - f(x))/h        #2pt method
    der3 = (f(x+h) - f(x-h))/(2*h)  #3pt method
    der5 = (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h))/(12*h)
    plt.plot(x, der2, 'gx')
    plt.plot(x, der3, 'r+')
    plt.plot(x, der5, 'b.')
    der_exact = 3.0*x**2 - 4.0*x - 5.0
    plt.plot(x, der_exact, 'y.-')
    x += h
    print '{0:8.3f}{1:8.3f}{2:8.3f}{3:8.3f}'.format(der2, der3, der5, der_exact)

plt.plot(x-h, der2, 'gx', label='2 pt method')
plt.plot(x-h, der3, 'r+', label='3 pt method')
plt.plot(x-h, der5, 'b.', label='5 pt method')
plt.plot(x-h, der_exact, 'y.-', label='Exact')
plt.legend(loc='upper left')
plt.show()
