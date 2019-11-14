import matplotlib.pyplot as plt
import math
import pylab


def f(x):
    return 9 * math.exp(-x) * math.sin(2 * math.pi * x) - 3.5


def df(x):
    return -9 * math.exp(-x) * math.sin(2 * math.pi * x) + 18 * math.pi * math.exp(-x) * math.cos(2 * math.pi * x)


def dx(f, x):
    return abs(0 - f(x))


def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0) / df(x0)
        delta = dx(f, x0)
        if x0 > 0:
            print('Root is at: ', x0)
            print('f(x) at root is: ', f(x0))


plt.axis([-10, 10, -10, 10])
plt.xlabel('x')
plt.ylabel('F(x)')
xs = []
vals = []
x = 0
while x < 100.0:
    vals += [f(x)]
    xs += [x]
    x += 0.01
plt.grid()
plt.plot(xs, vals, color='blue', linestyle='solid',
         label='sin(x)')
pylab.show()
x0s = [0.0, 0.1]
for x0 in x0s:
    newtons_method(f, df, x0, 1e-6)
print("Visit my github page with another lab.works: https://github.com/hellcoder09/2CourseProjects")
print("©Sagdeev Emil")

