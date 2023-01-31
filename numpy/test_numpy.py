# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:35:16 2023

@author: 459
"""

import numpy as np
from numpy import linalg as la

cc = la.norm([5, 6])
print("norm is ", cc)

x =  13.43420437374
print ("flor is round to down", np.floor(x))

print ("flor is round to up", np.ceil(x))


print ("flor is round", np.round(x, 3))

lst = [1,3,4, 5,6]
print ("print lst ", type(lst), lst)


print ("print lst npy ", type(np.array(lst)), np.array(lst))

toNpArray = np.array(lst) 

print ("toNpshape diamension ", toNpArray.shape)

print ("toNpArray is ", np.array(lst))


def func (x, y):
    print(x,y)
    return None

def func2 (x, y, z=4):
    print(x,y)
    return None

#call func 
func(1,2)
#call func2 without z param as z param is initilzed s
func2(x=1, y=3)
