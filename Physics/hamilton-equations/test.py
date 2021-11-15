#!/usr/bin/env python

import numpy as np


def w3(n, y):
    return (n + 0.5) * np.pi * np.sqrt(y)


x_values = np.arange(-1, 1, 0.01)
y_values = []

set_n = 1

for x in x_values:
    y_values.append(w3(1, x))

for id in range(len(x_values)):
    print(x_values[id], y_values[id])
