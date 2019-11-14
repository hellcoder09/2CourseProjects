import math
def f(x):
    return -25+82*x-90*pow(x,2)+44*pow(x,3)-8*pow(x,4)+0.7*pow(x,5)
def MDP(f, a, b, e, p):
    while abs(b - a) >= e:
        if p == 1:
            x = (a + b) / 2.0
            fx = f(x)
            fa = f(a)
            if (fx < 0 and fa < 0) or (fx > 0 and fa > 0):
                a = x
            else:
                b = x
        else:
            x = a*f(b)

    return x
x = MDP(f, -1, 1, 1e-8, 1)
print("Корень:",x)
print("Значение функции:",f(x))
print("Visit my github page with another lab.works: https://github.com/hellcoder09/2CourseProjects")
print("©Sagdeev Emil")
