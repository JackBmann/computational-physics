'''
decay.py
solve for radioactive decay of parent and daughter nuclei
9/22/16
'''
import matplotlib.pyplot as plt

#initial conditions
t = 0
N1 = input("Enter the number of the parent nuclei: ")
N2 = 0
k1 = input("Enter the decay constant for the parent nuclei: ")
k2 = input("Enter the decay constant for the daughter nuclei: ")
tstop = 300
h = 0.05

def dN1_dt(N1):
    return -k1*N1

def dN2_dt(N1, N2):
    return k1*N1 - k2*N2

plt.plot(t, N1, 'r+', label="Parent")
plt.plot(t, N2, 'go', label="Daughter")

#implement the Euler Algorithm
while t <= tstop:
    plt.plot(t, N1, 'r+')
    plt.plot(t, N2, 'go')

    #implement Euler
    N2 += dN2_dt(N1, N2)*h
    N1 += dN1_dt(N1)*h

    t += h

plt.legend(loc="upper right")
plt.show()
