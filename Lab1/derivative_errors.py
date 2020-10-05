from math import *
import matplotlib.pyplot as plt
plt.style.use("ggplot")

def f1(x):
    return sin(x*x)

def df1(x):
    return 2*x*cos(x*x)


def f2(x):
    return cos(sin(x))

def df2(x):
    return -sin(sin(x))*cos(x)


def f3(x):
    return exp(sin(cos(x)))

def df3(x):
    return -exp(sin(cos(x)))*cos(cos(x))*sin(x)


def f4(x):
    return log(x + 3)

def df4(x):
    return 1 / (x + 3)


def f5(x):
    return sqrt(x + 3)

def df5(x):
    return 1 / (2*sqrt(x + 3))


# point
x0 = 5.0

def method1(f, h):
    return (f(x0 + h) - f(x0)) / h

def method2(f, h):
    return (f(x0) - f(x0 - h)) / h

def method3(f, h):
    return (f(x0 + h) - f(x0 - h)) / (2*h)

def method4(f, h):
    return 2*(f(x0 + h) - f(x0 - h)) / (3*h) - \
           (f(x0 + 2*h) - f(x0 - 2*h)) / (12*h)

def method5(f, h):
    return 3*(f(x0 + h) - f(x0 - h)) / (4*h) - \
           3*(f(x0 + 2*h) - f(x0 - 2*h)) / (20*h) + \
           (f(x0 + 3*h) - f(x0 - 3*h)) / (60*h)


max_n = 21
hrange = [1 / pow(2, n - 1) for n in range(1, max_n)]


# Derivative of function 1
y1 = [fabs(method1(f1, hn) - df1(x0)) for hn in hrange]
y2 = [fabs(method2(f1, hn) - df1(x0)) for hn in hrange]
y3 = [fabs(method3(f1, hn) - df1(x0)) for hn in hrange]
y4 = [fabs(method4(f1, hn) - df1(x0)) for hn in hrange]
y5 = [fabs(method5(f1, hn) - df1(x0)) for hn in hrange]

fig1, graph1 = plt.subplots(figsize=(9, 5))

graph1.set_title("Derivative of function 1")
graph1.set_xlabel("h")
graph1.set_ylabel("Absolute error")

graph1.set_xscale('log')
graph1.set_yscale('log')

plt.plot(hrange, y1, "k--*", label="method1")
plt.plot(hrange, y2, "b--*", label="method2")
plt.plot(hrange, y3, "r--*", label="method3")
plt.plot(hrange, y4, "c--*", label="method4")
plt.plot(hrange, y5, "m--*", label="method5")

plt.legend()


# Derivative of function 2
y1 = [fabs(method1(f2, hn) - df2(x0)) for hn in hrange]
y2 = [fabs(method2(f2, hn) - df2(x0)) for hn in hrange]
y3 = [fabs(method3(f2, hn) - df2(x0)) for hn in hrange]
y4 = [fabs(method4(f2, hn) - df2(x0)) for hn in hrange]
y5 = [fabs(method5(f2, hn) - df2(x0)) for hn in hrange]

fig2, graph2 = plt.subplots(figsize=(9, 5))

graph2.set_title("Derivative of function 2")
graph2.set_xlabel("h")
graph2.set_ylabel("Absolute error")

graph2.set_xscale('log')
graph2.set_yscale('log')

plt.plot(hrange, y1, "k--*", label="method1")
plt.plot(hrange, y2, "b--*", label="method2")
plt.plot(hrange, y3, "r--*", label="method3")
plt.plot(hrange, y4, "c--*", label="method4")
plt.plot(hrange, y5, "m--*", label="method5")

plt.legend()


# Derivative of function 3
y1 = [fabs(method1(f3, hn) - df3(x0)) for hn in hrange]
y2 = [fabs(method2(f3, hn) - df3(x0)) for hn in hrange]
y3 = [fabs(method3(f3, hn) - df3(x0)) for hn in hrange]
y4 = [fabs(method4(f3, hn) - df3(x0)) for hn in hrange]
y5 = [fabs(method5(f3, hn) - df3(x0)) for hn in hrange]

fig3, graph3 = plt.subplots(figsize=(9, 5))

graph3.set_title("Derivative of function 3")
graph3.set_xlabel("h")
graph3.set_ylabel("Absolute error")

graph3.set_xscale('log')
graph3.set_yscale('log')

plt.plot(hrange, y1, "k--*", label="method1")
plt.plot(hrange, y2, "b--*", label="method2")
plt.plot(hrange, y3, "r--*", label="method3")
plt.plot(hrange, y4, "c--*", label="method4")
plt.plot(hrange, y5, "m--*", label="method5")

plt.legend()


# Derivative of function 4
y1 = [fabs(method1(f4, hn) - df4(x0)) for hn in hrange]
y2 = [fabs(method2(f4, hn) - df4(x0)) for hn in hrange]
y3 = [fabs(method3(f4, hn) - df4(x0)) for hn in hrange]
y4 = [fabs(method4(f4, hn) - df4(x0)) for hn in hrange]
y5 = [fabs(method5(f4, hn) - df4(x0)) for hn in hrange]

fig4, graph4 = plt.subplots(figsize=(9, 5))

graph4.set_title("Derivative of function 4")
graph4.set_xlabel("h")
graph4.set_ylabel("Absolute error")

graph4.set_xscale('log')
graph4.set_yscale('log')

plt.plot(hrange, y1, "k--*", label="method1")
plt.plot(hrange, y2, "b--*", label="method2")
plt.plot(hrange, y3, "r--*", label="method3")
plt.plot(hrange, y4, "c--*", label="method4")
plt.plot(hrange, y5, "m--*", label="method5")

plt.legend()


# Derivative of function 5
y1 = [fabs(method1(f5, hn) - df5(x0)) for hn in hrange]
y2 = [fabs(method2(f5, hn) - df5(x0)) for hn in hrange]
y3 = [fabs(method3(f5, hn) - df5(x0)) for hn in hrange]
y4 = [fabs(method4(f5, hn) - df5(x0)) for hn in hrange]
y5 = [fabs(method5(f5, hn) - df5(x0)) for hn in hrange]

fig5, graph5 = plt.subplots(figsize=(9, 5))

graph5.set_title("Derivative of function 5")
graph5.set_xlabel("h")
graph5.set_ylabel("Absolute error")

graph5.set_xscale('log')
graph5.set_yscale('log')

plt.plot(hrange, y1, "k--*", label="method1")
plt.plot(hrange, y2, "b--*", label="method2")
plt.plot(hrange, y3, "r--*", label="method3")
plt.plot(hrange, y4, "c--*", label="method4")
plt.plot(hrange, y5, "m--*", label="method5")

plt.legend()


plt.show()
