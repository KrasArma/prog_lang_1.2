
import numpy as np
import matplotlib.pyplot as plt


X = float(input('введите X: '))
Y = float(input('введите Y: '))

def f_1(x):
    return 2*x + 1

def f_2(x):
    return -3*x + 2

y = [-3] * 2

if Y <= f_1(X) and Y <= f_2(X) and Y >= -3:
    print('True')
else:
    print('False')

x = np.linspace(-10, 10, 2)
plt.scatter(X, Y, color= 'navy')

plt.plot(x, f_1(x), linestyle= '-', linewidth= 2, color= 'dodgerblue', label= '$y=2*x + 1$')
plt.plot(x, f_2(x), linestyle= '-', linewidth= 2, color= 'steelblue', label= '$y=-3*x + 2$')
plt.plot(x, y, linestyle= '-', linewidth= 2, color= 'darkturquoise', label= '$y=-3$')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.show()


