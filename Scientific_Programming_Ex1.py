import numpy as np
from sympy import *
import math

def Q1(a=0, b=1):
    epsilon = 10 ** -6
    c = (b + a) / 2

    def func(num):
        return 3 * num + math.sin(num) - math.exp(num)

    while abs(func(c)) > epsilon:
        c = (b + a) / 2
        flag_a = math.copysign(1, func(a))
        flag_c = math.copysign(1, func(c))
        if flag_a == flag_c:
            a = c
        else:
            b = c
        norma = "%.15f" % abs(func(c))
        print(f"c is equal to {c} and norma is {norma}")


def Q2():
    def f1(x, y, z):
        return (x * y) - (z ** 2) - 1

    def f2(x, y, z):
        return (x * y * z) + (y ** 2) - (x ** 2) - 2

    def f3(x, y, z):
        return (math.e ** x) + z - (math.e ** y) - 3

    Vector = [1, 2, 1]
    symbs = list(symbols('x, y, z'))
    norma = 100
    epsilon = 10**-6
    while norma > epsilon:
        f1_derivatives = [diff(f1(symbs[0], symbs[1], symbs[2]), symbs[0]), diff(f1(symbs[0], symbs[1], symbs[2]), symbs[1]), diff(f1(symbs[0], symbs[1], symbs[2]), symbs[2])]
        f2_derivatives = [diff(f2(symbs[0], symbs[1], symbs[2]), symbs[0]), diff(f2(symbs[0], symbs[1], symbs[2]), symbs[1]), diff(f2(symbs[0], symbs[1], symbs[2]), symbs[2])]
        f3_derivatives = [diff(f3(symbs[0], symbs[1], symbs[2]), symbs[0]), diff(f3(symbs[0], symbs[1], symbs[2]), symbs[1]), diff(f3(symbs[0], symbs[1], symbs[2]), symbs[2])]
        Jcb = [f1_derivatives, f2_derivatives, f3_derivatives]
        for i in range(len(Jcb)):
            for j in range(len(f1_derivatives)):
                Jcb[i][j] = Jcb[i][j].subs(symbs[0], Vector[0])
                Jcb[i][j] = Jcb[i][j].subs(symbs[1], Vector[1])
                Jcb[i][j] = Jcb[i][j].subs(symbs[2], Vector[2])
        MatrixMultRes = np.dot(Jcb, symbs)
        answers = solve([Eq(MatrixMultRes[0], -1 * f1(Vector[0], Vector[1], Vector[2])), Eq(MatrixMultRes[1], -1 * f2(Vector[0], Vector[1], Vector[2])), Eq(MatrixMultRes[2], -1 * f3(Vector[0], Vector[1], Vector[2]))], symbs)
        Vector[0] += answers[symbs[0]]
        Vector[1] += answers[symbs[1]]
        Vector[2] += answers[symbs[2]]
        norma = math.sqrt(f1(Vector[0], Vector[1], Vector[2]) ** 2 + f2(Vector[0], Vector[1], Vector[2]) ** 2 + f3(Vector[0], Vector[1], Vector[2]) ** 2)
        print(f"Vector answer is {Vector} and its norma is equal to {norma}")


if __name__ == '__main__':
    print("Solving the first question...")
    Q1(0, 1)
    print("Solving the second question...")
    Q2()
    print("Done solving questions.")
