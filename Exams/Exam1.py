'''
Exam1.py
completes the Exam 1 problems
9/23/16
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
import math
from mpl_toolkits.mplot3d import Axes3D

#Problem 1
p = raw_input("Enter a line of text: ")
print p
f = float(input("Please enter a float: "))
print f

#Problem 2
num1 = 5
if num1 >= 91:
    num2 = 3
else: 
    if num1 < 6:
        num2 = 4
    else:
        num2 = 2
x = num2 * num1 + 1
print (x,x%7)

#Problem 3
for i in range(1,10): 
    print "i = ", i
i = 1
while i < 10:
    print "i = ", i
    i += 1

#Problem 4
i = 20
while (i > 0): 
    print "i = ", i 
    i = i - 1
for i in range(20, 0, -1):
    print "i = ", i

#Problem 5
#1/l=R(1/(n^2)-1/(m^2))
R = 1.097*10**-2
for n in range(1, 4):
    for m in range(n+1, n+5):
        l = 1.0/(R*(1/float(n)**2 - 1/float(m)**2))
        print "For n = {0} and m = {1}, the wavelength is {2:.4f}".format(n, m, l)

#Problem 6
#f(x^2) = 1/(2^(v/2) * gamma(v/2)) * e^(x^2/2) * (x^2)^(v/2 - 1)
def chisquare(x, v):
    return (1/((2**(v/2)) * special.gamma(v/2))) * (np.e)**(-x/2) * x**((v/2)-1)
xs = []
f4 = []
f10 = []
for n in range(0, 29):
    xs.append(n)
for x in xs:
    f4.append(chisquare(x, 4))
plt.plot(xs, f4, "bo", label="v = 4")
for x in xs:
    f10.append(chisquare(x, 10))
plt.plot(xs, f10, "ko", label="v = 10")
plt.xlabel("X^2 value")
plt.ylabel("f(X^2) value")
plt.legend(loc="best")
print "The peak values for v=4 and v=10 are {0:5.5f} and {1:5.5f}, respectively.".format(max(f4), max(f10)) 
plt.show()

#Problem 7
#Part 1
data = np.loadtxt("Problem7Data.txt", skiprows=1)
independent = data[:, 0]
dependent = data[:, 1]
error = data[:, 2]
N = len(dependent)

#Part 2
avg_dependent = 0.0
for d in dependent:
    avg_dependent += d
avg_dependent /= N
print "The average value of the dependent variable (Air Mass) is: ", avg_dependent

#Part 3
std_dependent = 0.0
for d in dependent:
    std_dependent += (d - avg_dependent)**2
std_dependent = math.sqrt(std_dependent/N)
print "The standard deviation of the dependent variable (Air Mass) is: ", std_dependent

#Part 4
sum_x = 0 #Independent/B-V
sum_y = 0 #Dependent/Air Mass
sum_xx = 0
sum_xy = 0
x_max = 0 #Maximum independent variable value
for i in range(0, N):
    if independent[i] > x_max:
        x_max = idependent[i]
    plt.plot(independent, dependent, "bo")
    sum_x += independent[i]
    sum_y += dependent[i]
    sum_xx += independent[i] * independent[i]
    sum_xy += independent[i] * dependent[i]
A = (sum_xx*sum_y - sum_x*sum_xy)/(N*sum_xx - sum_x*sum_x)
B = (N*sum_xy - sum_x*sum_y)/(N*sum_xx - sum_x*sum_x)

#Part 5
plt.errorbar(independent, dependent, xerr=np.std(dependent)/N, fmt="b.", label="Data and error bars")
x_calc = np.linspace(-0.85, -0.64)
y_calc = A + B*x_calc

#Part 6
plt.plot(x_calc, y_calc, "r-", label="Best fit line")

#Part 7
print "The least squares fit for a straight line to the data is: y = {0:5.2f} + {1:5.2f}x".format(A, B)
plt.xlabel("B-V")
plt.ylabel("Air Mass")
plt.legend(loc="best")
plt.show()

#Part 8
y_residual = dependent - (A + B*independent)
plt.plot(independent, y_residual, "gx", label="Residual values")
plt.xlabel("B-V Residual Vales")
plt.ylabel("Air Mass")
plt.legend(loc="best")
plt.show()

#Problem 8
data = np.loadtxt("Problem8Data.csv", skiprows=6, delimiter=',')
time = data[:, 0]
rx = data[:, 49]
ry = data[:, 50]
rz = data[:, 51]
lx = data[:, 67]
ly = data[:, 68]
lz = data[:, 69]
rvx = [0]
rvy = [0]
rvz = [0]
lvx = [0]
lvy = [0]
lvz = [0]
rax = [0, 0]
ray = [0, 0]
raz = [0, 0]
lax = [0, 0]
lay = [0, 0]
laz = [0, 0]
for t in range(1, len(time)):
    rvx.append((rx[t] - rx[t-1])/(time[t]-time[t-1]))
    rvy.append((ry[t] - ry[t-1])/(time[t]-time[t-1]))
    rvz.append((rz[t] - rz[t-1])/(time[t]-time[t-1]))
    lvx.append((lx[t] - lx[t-1])/(time[t]-time[t-1]))
    lvy.append((ly[t] - ly[t-1])/(time[t]-time[t-1]))
    lvz.append((lz[t] - lz[t-1])/(time[t]-time[t-1]))
for t in range(1, len(time)-1):
    rax.append((rvx[t] - rvx[t-1])/(time[t]-time[t-1]))
    ray.append((rvy[t] - rvy[t-1])/(time[t]-time[t-1]))
    raz.append((rvz[t] - rvz[t-1])/(time[t]-time[t-1]))
    lax.append((lvx[t] - lvx[t-1])/(time[t]-time[t-1]))
    lay.append((lvy[t] - lvy[t-1])/(time[t]-time[t-1]))
    laz.append((lvz[t] - lvz[t-1])/(time[t]-time[t-1]))

#3D Figure
fig = plt.figure()
graph = fig.gca(projection='3d')
graph.plot(rx, ry, rz, label="Right Knee Position")
graph.plot(lx, ly, lz, label="Left Knee Position")
graph.plot(rvx, rvy, rvz, label="Right Knee Velocity")
graph.plot(lvx, lvy, lvz, label="Left Knee Velocity")
graph.plot(rax, ray, raz, label="Right Knee Acceleration")
graph.plot(lax, lay, laz, label="Left Knee Acceleration")
plt.legend(loc='best')
plt.show()

#2D Figures
plt.figure()
plt.subplot(321)
plt.xlabel("Time (s)")
plt.ylabel("Right Foot Position (m)")
plt.plot(time, rx, 'ro', label='x')
plt.plot(time, ry, 'wo', label='y')
plt.plot(time, rz, 'bo', label='z')
plt.legend(loc="best")
plt.subplot(323)
plt.xlabel("Time (s)")
plt.ylabel("Right Foot Velocity (m/s)")
plt.plot(time, rvx, 'ro', label='x')
plt.plot(time, rvy, 'wo', label='y')
plt.plot(time, rvz, 'bo', label='z')
plt.legend(loc="best")
plt.subplot(325)
plt.xlabel("Time (s)")
plt.ylabel("Right Foot Acceleration (m/s^2)")
plt.plot(time, rax, 'ro', label='x')
plt.plot(time, ray, 'wo', label='y')
plt.plot(time, raz, 'bo', label='z')
plt.legend(loc="best")
plt.subplot(322)
plt.xlabel("Time (s)")
plt.ylabel("Left Foot Position (m)")
plt.plot(time, lx, 'ro', label='x')
plt.plot(time, ly, 'wo', label='y')
plt.plot(time, lz, 'bo', label='z')
plt.legend(loc="best")
plt.subplot(324)
plt.xlabel("Time (s)")
plt.ylabel("Left Foot Velocity (m/s)")
plt.plot(time, lvx, 'ro', label='x')
plt.plot(time, lvy, 'wo', label='y')
plt.plot(time, lvz, 'bo', label='z')
plt.legend(loc="best")
plt.subplot(326)
plt.xlabel("Time (s)")
plt.ylabel("Left Foot Acceleration (m/s^2)")
plt.plot(time, lax, 'ro', label='x')
plt.plot(time, lay, 'wo', label='y')
plt.plot(time, laz, 'bo', label='z')
plt.legend(loc="best")
plt.show()
