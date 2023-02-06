# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 18:06:07 2023

@author: 459
"""


import numpy as np
import matplotlib.pyplot as plt

# metric to evaluate model  [mean_squared_error, mean_absolute_error - > small No is better]
#r2_score large No is better
from sklearn.metrics import  mean_squared_error, mean_absolute_error, r2_score

# liner model ready least square model
from sklearn.linear_model import LinearRegression

## preprocessing
from sklearn.preprocessing import PolynomialFeatures
# using square ^2
X = 6 * np.random.rand(100, 1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)




## we need to handle non-linear Regression to fit in this data
## we will used what is called (Polynomial Regression)

## dgree 2 is no of dimationtion will generate no of compinations 
## Get the polynomial Features --> it will generate combination of new features according to required degree and number of features
poly_features = PolynomialFeatures(degree=2, include_bias=False)  ## an instance of the class

## fit the instance to the dataset and transform to new features which the model will be trained on
# generate x^2 and x@x ...
X_poly = poly_features.fit_transform(X)

print('X[0] --> ', X[0])
print('X_poly[0] --> ', X_poly[0])  ## return (X & X^2)



print (y)
# new instance of LinearRegression + iit will add [1,1,1,1,1,] by default
ln = LinearRegression()
# start training  on X_poly
ln.fit(X_poly, y)
###################Training has been done let we get thetas #################
print ("theta 1" , ln.coef_)
print ("theta 0" , ln.intercept_)
############################# let we apply prediction ################
y_pred = ln.predict(X_poly)

print("y_pred my prediction is ", y_pred)

mean_squared_error  = mean_squared_error(y, y_pred)

print("  metric mean_squared_error ", mean_squared_error)


plt.plot(X, y, "bo")
plt.plot(X,y_pred , "r")
