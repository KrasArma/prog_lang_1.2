
import scipy
import numpy as np
import matplotlib.pyplot as plt


a = float(input('введите нижний предел: '))
b = float(input('введите верхний предел: '))
n = int(input('введите количество точек: '))

x = np.linspace(a, b, n)
x1 = np.linspace(a,b,200)
y_rectangle = []
y_trapezoid = []
y_Simpson = []

def func(x):
    return ((x**2)*np.sin(x))/10


def integral():
    return scipy.integrate.quad(func,a,b)


def m_rectangle(a,b,p):
    summa_1 = 0
    h1 = (b-a)/p
    x = np.linspace(a, b, p)
    for i in range(p):
        summa_1 += func(x[i])
    return h1 * summa_1


def m_trapezoid(a,b,p):
    summa_2 = 0
    h1 = (b-a)/p
    x = np.linspace(a, b, p)
    for i in range(p):
        summa_2 += func((x[i]+x[i-1])/2)
    return h1 * summa_2


def m_Simpson(a,b,p):
    X = np.linspace(a, b, 2*p)
    summa_3 = func(X[0]) + func(X[2*p-1])
    h2 = (b-a)/(2*p)

    for i in range(0,2*p - 2,2):
        summa_3 += 2*func(X[i])
    for j in range(0,2*p - 1,2):
        summa_3 += 4*func(X[j])
    return (h2 * summa_3)/3


for p in range(2,1000,5):
    y_rectangle.append(m_rectangle(a,b,p))
    y_trapezoid.append(m_trapezoid(a,b,p))
    y_Simpson.append(m_Simpson(a,b,p))

print()
print('значение интеграла: ', integral(x))
print()
print('значение по методу прямоугольников: ', m_rectangle(a,b,n))
print('значение по методу трапеций: ', m_trapezoid(a,b,n))
print('значение по методу Симпсона: ', m_Simpson(a,b,n))

plt.plot(x1, y_rectangle, linestyle= '--', linewidth= 2, color= 'dodgerblue', label= 'м. прямоугольников')
plt.scatter(x1, y_trapezoid, linewidth= 0.2, color= 'steelblue', label= 'м. трапеций')
plt.plot(x1, y_Simpson, "v", linewidth= 0.1, color= 'darkturquoise', label= 'м. Симпсона')


plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='lower right')
plt.show()
