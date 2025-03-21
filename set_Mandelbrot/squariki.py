from math import cos, sin, acos

def upgrade_range(start, stop, step):
    x = []
    while start <= stop:
        start += step
        x.append(start)
    return x

def C(x, y):
    return complex(x, y)


def square_complex(x, y):
    if x == 0 and y == 0:
        return 0 + 0j
    absz = ((x ** 2) + (y ** 2)) ** 0.5
    z = (absz ** 4) * (cos(2 * acos(x / absz)) + sin(2 * acos(x / absz)) * 1j)
    return z

