def f(x,y,z):
    return (x+10)**2 + (y-3)**2 + (1-z)**2

def dx_f(x):
    return 2*(x+10)

def dy_f(y):
    return 2*(y-3)

def dz_f(z):
    return 2*(z-1)

L = 0.0001
epochs = 1000000

x = 0
y = 0
z = 0

for i in range(epochs):
    d_x = dx_f(x)
    d_y = dy_f(x)
    d_z = dz_f(x)

    x = x - L * d_x
    y = y - L * d_y
    z = z - L * d_z

print(x,y,z,f(x,y,z))
