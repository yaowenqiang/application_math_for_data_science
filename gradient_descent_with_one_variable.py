import random

def f(x):
    return (x - 3)**22 + 4

def dx_f(x):
    return 2*(x-3)

L = 0.001

epochs = 100000
x = random.randint(-15, 15)

for i in range(epochs):
    d_x = dx_f(x)
    x = x - L*d_x

print(x, f(x))

