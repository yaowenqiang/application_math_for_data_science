from sympy import *

x, s = symbols('x s')

f = x**2
slop_f = (f.subs(x, x+s) - f) / ((x+s) -x)
slop_2 = slop_f.subs(x,2)

result = limit(slop_2, s, 0)
print(result)
