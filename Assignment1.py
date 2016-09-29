'''
Assignment1.py
This file completes Assignment 1.
8/25/16
version 1.0
'''

#Problem 1
print "Problem 1"
#y = 0.5*g*t^2 + v_0*t + y_0
#v = g*t
#y = 0.5*g*t^2
g = -9.81
#t = input("Enter the time: ") #x = int(raw_input("Enter x: "))
t = 1.2
y = .5*g*t**2
v = g*t
print "(a) y:", y, "v:", v
t = 3.6
y = .5*g*t**2
v = g*t
print "(b) y:", y, "v:", v
t = 6.0
y = .5*g*t**2
t = 5.0
v = g*t
print "(c) y:", y, "v:", v


#Problem 2
print "\nProblem 2"
sec = 1.0E9
age = sec/60/60/24/365.25
if age < 80:
    print "Yes,", sec, " =", age, "years"
else:
    print "No,", sec, " =", age, "years"

#Problem 3
print "\nProblem 3"
A = 1000
p = .025
n = 5
val = A*(1+p/100)**n
print "The value of the account in " + str(n) + " years is $" + str(val)
n = 10
val = A*(1+p/100)**n
print "The value of the account in " + str(n) + " years is $" + str(val)
n = 30
val = A*(1+p/100)**n
print "The value of the account in " + str(n) + " years is $" + str(val)

#Problem 4
print "\nProblem 4"
v0 = 3
t = 2
a = 2
x = v0*t + (1./2)*a*t**2
#print a #to obtain the correct answer for x, this line must be changed to: print x
print x

#Problem 5
print "\nProblem 5"
#a = 2; b = 1; c = 2 #there is no real solution for x using these constants
a = 1; b = 2; c = 1
from math import sqrt
q = sqrt(b*b - 4*a*c)
#x1 = (-b + q)/2*a #This line is dividing prior to multiplying it should be: x1 = (-b + q)/(2*a)
x1 = (-b + q)/(2*a)
#x2 = (-b - q)/2*a #This line is dividing prior to multiplying it should be: x2 = (-b-q)/(2*a)
x2 = (-b - q)/(2*a)
print "a", x1, x2

#Problem 6
print "\nProblem 6"
a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b
print c #this prints out all of the values in a AND b
b[0] = -1
d = [e+1 for e in a]
print d #this adds one to each value of a and prints them out
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2] #this prints out the second to last value of d, which is 0, because after b[0] was set to -1 b[0]+1 was appended to d and then another value was appended to d

#Problem 7
print "\nProblem 7"
directory_path = "/usr/data/"
for x in range(1, 101, 1):
    print directory_path + "data" + str(x).zfill(3) + ".txt"
    #if(x < 10):
    #    print directory_path + "data00" + str(x)
    #elif(x < 100):
    #    print directory_path + "data0" + str(x)
    #else:
    #    print directory_path + "data" + str(x)

#Problem 8
print "\nProblem 8"
from math import sin, factorial
val = 0
n = 100
x = 90
for j in range(0, n, 1):
    val = val + pow(-1, j)*pow(x, 2*j+1)/factorial(2*j+1) #this infinite series for calculating sin is wrong
print "Our value of sin(x) is:       ", val
print "The Python value of sin(x) is:", sin(x)

#Problem 9
print "\nProblem 9"
#n = input("Enter the number of Fibonacci numbers to print: ")
n = 10
fibs = [0, 1]
for y  in range(2, n, 1):
    fibs.append(fibs[y-2] + fibs[y-1])
print fibs

#Problem 10
print "\nProblem 10"
#n = input("Enter a natural number: ")
n = 10
iterates = [n]
for z in range(0, 20, 1):
    if(n % 2 == 0):
        n = n/2
    else:
        n = (3*n + 1)
    iterates.append(n)
print iterates