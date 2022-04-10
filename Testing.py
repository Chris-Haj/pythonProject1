import math
import sympy as sy
from sympy import *
import numpy as np

def fun1(x, y, z):
    return (x * y) - (z ** 2) - 1


def derivative1(x, y, z, a):
    if a == 'x':
        return y
    elif a == 'y':
        return x
    elif a == 'z':
        return -2 * z


def fun2(x, y, z):
    return (x * y * z) + (y ** 2) - (x ** 2) - 2


def derivative2(x, y, z, a):
    if a == 'x':
        return (y * z) - (2 * x)
    elif a == 'y':
        return (x * z) + (2 * y)
    elif a == 'z':
        return x * y


def fun3(x, y, z):
    return (math.e ** x) + z - (math.e ** y) - 3


def derivative3(x, y, z, a):
    if a == 'x':
        return math.e ** x
    elif a == 'y':
        return -1 * (math.e ** y)
    elif a == 'z':
        return 1


def solve_system():
    res = [1, 2, 1]
    x1, x2, x3 = symbols('x1, x2, x3')
    delta = [x1, x2, x3]
    norma = 10
    # while norma >= math.pow(10, -6):
    jacobian = [[derivative1(res[0], res[1], res[2], 'x'), derivative1(res[0], res[1], res[2], 'y'),
                 derivative1(res[0], res[1], res[2], 'z')],
                [derivative2(res[0], res[1], res[2], 'x'), derivative2(res[0], res[1], res[2], 'y'),
                 derivative2(res[0], res[1], res[2], 'z')],
                [derivative3(res[0], res[1], res[2], 'x'), derivative3(res[0], res[1], res[2], 'y'),
                 derivative3(res[0], res[1], res[2], 'z')]]
    print(jacobian)
    b = np.dot(jacobian, delta)
    a = solve([Eq(b[0], -1*fun1(res[0], res[1], res[2])), Eq(b[1], -1*fun2(res[0], res[1], res[2])), Eq(b[2], -1*fun3(res[0], res[1], res[2]))], [x1, x2, x3])
    print()
    x, y, z = a[x1], a[x2], a[x3]
    res = [x + res[0], y + res[1], z + res[2]]
    norma = math.sqrt(fun1(res[0], res[1], res[2])**2 + fun2(res[0], res[1], res[2])**2 + fun3(res[0], res[1], res[2])**2)
    print(res)


if __name__ == '__main__':
    solve_system()