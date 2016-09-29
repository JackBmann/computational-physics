'''
sin.py
Calculates sine(x) from a series
8/30/2016
'''
from math import sin, factorial

val = 0
n = input("Enter the number of terms n: ")
x = input("Enter the value of x: ")

for j in range(0, n, 1):
    val = val + pow(-1, j)*pow(x, 2*j+1)/factorial(2*j+1)
print "Our value of sin(x) is:       ", val
print "The Python value of sin(x) is:", sin(x)