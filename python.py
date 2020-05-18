import matplotlib.pyplot as plt
import numpy as np
import math


def desired_func(xx):
    return math.sin(xx)


def f(xx, yy):
    return math.cos(xx)


# xjpo - Xj+1
# xkpo - Xk+1
def iteration(yj, h, xjpo):
    eps = 1
    yk = yj
    while eps > 0.0001:
        ykpo = yj + h * f(xjpo, yk)
        # print("eps:", eps)
        eps = ykpo - yk
        yk = ykpo
    return yk


# def bdf3(p, righthandside, y0):
#


def backward_differentiation_formula(amount_of_points, h, x, y0):
    k = 1
    y = [y0]
    while k < amount_of_points:
        y.append(iteration(y[len(y) - 1], h, x[k]))
        k += 1
    print("Start approximate values: ", y)
    y_fpi = y.copy()
    k = 2
    while k < amount_of_points - 1:
        y[k+1] = (6/11)*(3*y[k]-(3/2)*y[k-1]+(1/3)*y[k-2]+h*f(x[k+1], y[k+1]))
        k += 1
    print("latest k = ", k)
    return y, y_fpi


fig, ax = plt.subplots()
amount_of_points = 101
x_min = -5
x_max = 5
x = np.linspace(x_min, x_max, amount_of_points)
h = (x_max - x_min)/(amount_of_points-1)
y0 = 0.95892427466
y, y_fpi = backward_differentiation_formula(amount_of_points, h, x, y0)
print("Y[] = ", y)
print("X[] = ", x)
y_exact = [y0]
i = 1
while i < amount_of_points:
    y_exact.append(desired_func(x[i]))
    i += 1
ax.plot(x, y, color='red', label='BDF')
ax.plot(x, y_fpi, color='green', label='Fixed-point-iteration')
ax.plot(x, y_exact, color='blue', label='Exact solution')
plt.grid()
plt.legend(loc='best');
plt.show()
