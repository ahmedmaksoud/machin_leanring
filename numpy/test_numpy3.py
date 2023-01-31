# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:22:38 2023

@author: 459
"""


import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt

randMat23 = np.random.randint(1,5,(2,3))
print("randMat23  ", randMat23)


randMat23 = np.random.randint(1,10,100)
print("randMat23  ", randMat23)


#plt.hist(randMat23, bins=5)

normalDistribuation = np.random.normal(loc=70,scale=20,size=10000)
print("randMat23  ", normalDistribuation)


plt.hist(normalDistribuation, bins=20)

