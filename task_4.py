
import numpy as np
import matplotlib.pyplot as plt

x0 = 0.5
Xarray = []


def func(x):
    return np.cos(x) - (x**3)


def d_func(x):
    return -np.sin(x) - 3 * (x**2)


def m_Nuton(f, d_f, xmain, e=1e-9):
    x = xmain

    while abs(f(x)) >= e:
        if d_f(x) == 0:
         break
        x = x - f(x) / d_f(x)

        Xarray.append(x)
    return x


print(m_Nuton(func, d_func, x0))
for i in range(len(d_func)):
    print('x= ', d_func[i], 'y= ', func(d_func[i]))

plt.axis([-10, 10, -10, 10])
plt.xlabel('x')
plt.ylabel('у')
plt.grid()
xdraw = np.linspace(-3, 3, 100)
plt.plot(xdraw, func(xdraw), color='green')
plt.plot(xdraw, d_func(xdraw), color='blue')
plt.plot(m_Nuton(func, d_func, x0))
for i in range(len(Xarray)):
    plt.plot(Xarray[i], func(Xarray[i]), 'ro')
    plt.plot(func(Xarray[i]), Xarray[i], 'b*')
plt.show()