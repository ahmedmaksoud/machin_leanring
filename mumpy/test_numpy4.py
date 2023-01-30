# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 21:19:01 2023

@author: 459
"""


import numpy as np

identyMstrix = np.eye(4)

print("identyMstrix 0 and 1 ", identyMstrix)

a = np.arange(12)
print("vector of 12 elements ", a)
a = a.reshape(2,6)

print("convert vector to matrix 2 6 ", a)

a = a.T

print("teanspose matix rows to olumns ", a)