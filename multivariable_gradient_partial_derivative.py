from sympy import *
x, y, z = symbols('x y z')

f = (x+10)**2 + (y-3)**2 + (1-z)**2

dx_f  = diff(f,x)
dy_f  = diff(f,y)
dz_f  = diff(f,z)

print(dx_f)
print(dy_f)
print(dz_f)
