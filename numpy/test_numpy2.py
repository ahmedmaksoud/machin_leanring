# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:07:44 2023

@author: 459
"""



import numpy as np
from numpy import linalg as la


lst = [[1,3,4, 5,6],[10,3,4, 6,7]] 

lst2 = np.array(lst)

print ("list diamension is ", lst2.shape)

print ("list diamension rows is ", lst2.shape[0])

print ("list diamension cols is ", lst2.shape[1])

print ("list row 0 ", lst2[0])
print ("list row 1 ", lst2[1])
print ("list col 0 ", lst2[:,0])
print ("list col 1 ", lst2[:,1])
print ("list element  0,3 ", lst2[0,3])
print ("list element  1,3 ", lst2[1,3])

emp = np.empty((3,4))

print ("list emp array 3* 4", emp)

emp2 = np.empty((3,4), dtype="int32")

print ("list emp2 array 3* 4", emp2)

zeros = np.zeros((3,3))

print ("list zeros", zeros)

cop = lst2.copy()

print ("list cop", cop)

listRange14No = list(range(14))

print ("list listRange14 Number ", listRange14No)



print ("list listRange14 Number ", np.random.randint(low=0, high=14,size= 14))


