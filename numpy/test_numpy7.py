# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:52:11 2023

@author: 459
"""


import numpy as np

### find x  ->>>> Ax=b 

#A_{3x3} b 3x1

#Ax=b
#x = InversAB
#x=A^-1b


A = np.random.randint(1,10,(3,3))
B = np.random.randint(1,10,(3,1))

x = np.linalg.inv(A).dot(B)

print("xxxxxxxxxx   ", x)

y = np.linalg.solve(A,B)

print("yyyyyyyyyyyyyy  ", y)