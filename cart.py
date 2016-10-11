import matplotlib.pyplot as plt

def a(v, t):
    return -v * R / m(t)

def m(t):
    return m_0 + R * t

t = 0
x = 0
v = 2
m_0 = 10
R = 50
h = 0.01

plt.figure()
plt.subplot(311)
plt.plot(t, x, 'ro', label='Position')
plt.legend(loc='best')
plt.subplot(312)
plt.plot(t, v, 'go', label='Velocity')
plt.legend(loc='best')
plt.subplot(313)
plt.plot(t, v, 'bo', label='Momentum')
plt.legend(loc='best')
while t <= 10:
    x += v * h
    v += a(v, t) * h
    t += h
    p = m(t) * v
    plt.subplot(311)
    plt.plot(t, x, 'ro')
    plt.subplot(312)
    plt.plot(t, v, 'go')
    plt.subplot(313)
    plt.plot(t, p, 'bo')

plt.legend(loc='upper left')
plt.show()
