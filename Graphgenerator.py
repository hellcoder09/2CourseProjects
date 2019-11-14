import matplotlib as mpl
import matplotlib.pyplot as plt
import math
def f(x):
    return -25+82*x-90*pow(x,2)+44*pow(x,3)-8*pow(x,4)+0.7*pow(x,5)
dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
xmin = -100
xmax = 100
ymin = -100
ymax = 100
mpl.rcParams.update({'font.size': 10})
plt.axis([xmin, xmax, ymin, ymax])
plt.title('graf')
plt.xlabel('x')
plt.ylabel('F(x)')
xs = []
ur_vals = []
x = xmin
while x < xmax:
    ur_vals += [f(x)]
    xs += [x]
    x += 0.1
plt.plot(xs, ur_vals, color = 'red', linestyle = 'dotted',
         label = 'x')
plt.grid(True)
plt.show()
plt.legend(loc = 'upper right')
fig.savefig('graf.png')
print("Visit my github page with another lab.works: https://github.com/hellcoder09/2CourseProjects")
print("©Sagdeev Emil")
