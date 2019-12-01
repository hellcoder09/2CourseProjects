import scipy.optimize
f= lambda x: (x[0]/(x[1]*(1-x[0])**2))**0.6+((1-x[0]/x[1])/(1-x[1])**2)**0.6+5*x[1]**(-0.6)
xopt = scipy.optimize.fmin(func=f, x0=[0.1,0.9])
print(xopt)
print("Visit my github page with another lab.works: https://github.com/hellcoder09/2CourseProjects")
print("©Sagdeev Emil")
