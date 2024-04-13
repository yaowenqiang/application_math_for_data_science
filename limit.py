from sympy import *

x = symbols('x')
f = 1 / x

result = limit(f, x, oo) # oo means infinity
print(result)
