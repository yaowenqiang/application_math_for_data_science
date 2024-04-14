from sympy import *
from sympy.plotting import plot3d

x = symbols('x')
f = x**2 * x**3
f1 = x**2 - 10
f2 = x**(1/2)

f3 =x **(1/3)
f4 =x **(-1/3)
f5 =x **(-2)
f6 =x **(-2)

x1, y1 = symbols('x1 y1')
f7 = 2*x1**2 * 3*y1**3
plot3d(f7)
plot(f5)
