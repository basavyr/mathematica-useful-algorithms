#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


def w3(n, y):
    try:
        assert y > 0
    except AssertionError as err:
        pass
    else:
        rez = (n + 0.5) * np.pi * np.sqrt(y)
        return rez


x_values = np.arange(-1, 1, 0.01)
y_values = []

set_n = 1

for x in x_values:
    try:
        assert x > 0
    except AssertionError as err:
        pass
    else:
        y_values.append(w3(set_n, x))

# make arrays ok
x_values = x_values[len(y_values):]

# for id in range(len(x_values)):
#     print(x_values[id], y_values[id])

dx_values = [abs(x_values[id]) - abs(x_values[id - 1])
             for id in range(1, len(x_values))]

dy_values = np.gradient(y_values, np.mean(dx_values))

with open('w3.dat', 'w+') as file:
    for dx in dx_values:
        file.write(str(dx) + '\n')

# compute the derivative of w3 function with respect to y
# dydx_values = np.gradient(y_values, dx_values)


# def plot_data(xdata, ydata, file):
#     plt.plot(xdata, ydata, label=f'n={set_n}')
#     plt.xlabel('y')
#     plt.ylabel(r'$w_3(n;y)$')
#     plt.legend(loc='best')
#     plt.savefig(file, bbox_inches='tight')
#     plt.close()


# def plot_f_df(xdata, ydata, dydata, file):
#     plt.plot(xdata, ydata, '-r', label=f'f')
#     plt.plot(xdata, dydata, '-ok', label=f'f\'')
#     plt.xlabel('y')
#     plt.ylabel('fcts')
#     plt.legend(loc='best')
#     plt.savefig(file, bbox_inches='tight')
#     plt.close()


# # plot_data(x_values, y_values, 'w3.pdf')
# # plot_data(np.arange(len(dx_values)), dx_values, 'w3_dx.pdf')
# plot_f_df(x_values, y_values, np.mean(dx_values), 'fcts_comparison.pdf')
