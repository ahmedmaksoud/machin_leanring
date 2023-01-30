# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 12:06:31 2023

@author: 459
"""

import numpy as np



aa = np.linspace(0, 10)

print("array of 50 elements with same sequnces in range like 1st element - 2ed = the same 2ed  - 3ed ", aa)

arr = np.array([[1,2,3,4,5,6],[9,8,7,4,5,6]])
sumArray = arr.sum()

print("arry = ", arr)

print("sum of arry = ", sumArray)


print("sum of matrix [rows] axis ", np.sum(arr, axis=1))

print("sum of matrix [rows] axis same above ", arr.sum( axis=1))

print("sum of matrix [columns] axis ", np.sum(arr, axis=0))

print("matrix reshape change rows/columns", arr.reshape(3, 4))

print("sum of dignaol الخط الي في النص", arr.trace())


arr2 = np.array([[1,2,3,4,5,6,5,7],[9,8,2,7,4,5,6,10]]) 
arr2 = arr2.reshape(4, 4)

print("sum of Determinant  ", np.linalg.det(arr2))

print("matrix invers  ", np.linalg.inv(arr2))

vect = [5,8,9]


print("vect  norm  1 ", np.linalg.norm(vect, ord=1))

print("vect  norm  2  (25 + 64 + 81)^1/2 ", np.linalg.norm(vect, ord=2))

print("vect  norm  defualt", np.linalg.norm(vect))


print("vect  eigen   (returns two parameters eigen values + eigen vector) ", np.linalg.eig(arr2))

k, v = np.linalg.eig(arr2)

print("vect  eigen    values  ", k)
print("vect  eigen    vector ", v)

print("matrix rand whic D it was 4 * 4   4d  ", np.linalg.matrix_rank(arr2))

arr3 = np.array([[1,3,5,7],[9,11,13,15],[2,5,6,8],[10,12,14,16]]) 

print("matrix rand whic D it was 4 * 4   خسرت   4d  becomes ", np.linalg.matrix_rank(arr3) , "d")

print("mean is ", np.mean(arr3))
print("mean is rows", np.mean(arr3, axis=1))
print("mean is columns", np.mean(arr3, axis=0))


print("statistics variance is ", np.var(arr3))
print("statistics standard divation is ", np.std(arr3))

feature1 = [1,6,8,2,9,3,6,2] 
feature2 = [2,12,9,10,11,12,13,14] 
print("statistics features covanice returns 2*2 matrix u shoud get [0,1] ", np.cov(feature1, feature2))

print("statistics features covanice ", np.cov(feature1, feature2)[0,1])

print("statistics features correlation ", np.corrcoef(feature1, feature2)[0,1])