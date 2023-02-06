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
from sklearn.linear_model import LinearRegression, SGDRegressor

X = 2 * np.random.rand(100,1)
y = 4 + 3 * X + np.random.rand(100,1)

print (y)
# new instance of SGDRegressor + it will add [1,1,1,1,1,] by default
sgd_reg = SGDRegressor()
# start training
sgd_reg.fit(X, y)


###################Training has been done let we get thetas #################
print ("theta 1" , sgd_reg.coef_)
print ("theta 0" , sgd_reg.intercept_)
############################# let we apply prediction ################
y_pred = sgd_reg.predict(X)

print("y_pred my prediction is ", y_pred)

mean_squared_error  = mean_squared_error(y, y_pred)

print("  metric mean_squared_error ", mean_squared_error)


plt.plot(X, y, "bo")
plt.plot(X,y_pred , "r")
