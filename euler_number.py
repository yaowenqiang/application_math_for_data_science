from math import exp, log
from sympy import *
x = 3
result = exp(x) # e^x
print(result)

result = log(x) # log(x)
print(result)

x1 = symbols('x')
f = exp(x1)
plot(f)

f2 = log(x)
plog(f2)
