# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:08:33 2023

@author: 459
"""
import numpy as np

X = 2 * np.random.rand(100,1)
Y = 3 * np.random.rand(100,1)

#print (X.shape ,  Y.T.shape)
c=  (X @ Y.T)

print (c.shape)

c2 =  X.dot(  Y.T)

print (c2.shape)

c3 = X * Y


print (c3.shape)

