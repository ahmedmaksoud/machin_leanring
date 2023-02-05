# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:42:31 2023

@author: 459
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 3 * x**2  + 4*x - 1

X_new = np.linspace(-5, 5)

print(X_new) 

y = f(X_new)

print("y is " , y)

plt.plot(X_new, y)