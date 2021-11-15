#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


def w3(n, y):
    return (n + 0.5) * np.pi * np.sqrt(y)


x_values = np.arange(-1, 1, 0.01)
y_values = []

set_n = 1

for x in x_values:
    y_values.append(w3(1, x))

for id in range(len(x_values)):
    print(x_values[id], y_values[id])


def plot_data(xdata, ydata, file):
    plt.plot(xdata, ydata, label=f'n={set_n}')
    plt.xlabel('y')
    plt.ylabel(r'$w_3(n;y)$')
    plt.legend(loc='best')
    plt.savefig(file, bbox_inches='tight')
    plt.close()


plot_data(x_values, y_values, 'w3.pdf')
