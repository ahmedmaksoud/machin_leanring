# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 14:43:19 2023

@author: 459
"""

import numpy as np

x = [1,6,8,2,9,3,6,2] 
y = [2,12,9,10,11,12,13,14] 





z = [2,12,9,10,11,12,13,14] 

q = np.column_stack((x, y, z))

print ("column_stack  convert to matrix 8*3" , q)

print ("max is " , q.max())


print ("max is " , q.max(axis=1))


x = [1,6,8,2,9,3,6,2] 

print ("max get index " , np.argmax(x))


q = np.column_stack((x, y))

print ("column_stack  convert to matrix 8*2" , q)
print ("concatenate" , np.concatenate((x, y)))

x1 = [[1,6,8,2,9,3,6,2], [1,6,8,2,9,3,6,2]]
y1 = [[2,12,9,10,11,12,13,14] ,[2,12,9,10,11,12,13,14] ]


print ("concatenate" , np.concatenate((x1, y1), axis=0))

print ("concatenate" , np.concatenate((x1, y1), axis=1))

mult1  = np.array([8,2,3]) 
mult2  = np.array([1,25,321]) 
multiply = mult1 @ mult2
print ("multi ply matrix " ,multiply )

print ("multi ply matrix " ,np.dot(x, y) )
xxx = np.dot(x, y)
print ("multi ply matrix " , xxx)

print ("multi ply matrix " ,np.dot(mult1, mult2) )
###################################################

mult1  = np.array([2,2,]) 
mult2  = np.array([3,5]) 
multiply = mult1 @ mult2
print ("multi ply matrix " ,multiply )