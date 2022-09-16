"""
Test solving 2D wave equation modes
"""

import numpy as np
import matplotlib.pyplot as plt


def test_soln(x, y, c=2000, lx=0.25, ly=0.25, a=1, n=1, m=1, t=0):
    z = a * np.sin(n*np.pi*x/lx) * np.sin(m*np.pi*y/ly)
    return z


if __name__ == '__main__':
    res = 250
    x_a = np.linspace(0, 0.25, res)
    y_a = np.linspace(0, 0.25, res)
    zeros = []
    for x in x_a:
        for y in y_a:
            z = test_soln(x=x, y=y)
            if z == 0.0:
                zeros.append((x,y))

    fig = plt.figure()
    for zero in zeros:
        plt.plot(zero[0], zero[1])
    plt.show()
