# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 20:46:16 2023

@author: 459
"""

import numpy as np
import matplotlib.pyplot as plt

data_single = np.genfromtxt('RegData.csv', delimiter=',')

X_ = data_single[:,0].reshape(-1,1)
y_ = data_single[:,1].reshape(-1,1)

thetas_single = np.zeros(2)

def predict_single(X, y, theta_input):
    
    h_theta = theta_input[0] + theta_input[1] * X
    
    return h_theta




def cost_single(X, y, theta_input):
    
    h_theta = predict_single(X, y, theta_input)
    
    h_y = (h_theta - y)**2
    j = np.sum(h_y) / (2* len(X))
    
    return j




def gradient_single(X, y, theta_input):
    
    h_theta = predict_single(X, y, theta_input)
    
    h_y_0 = h_theta - y 
    h_y_1 = (h_theta - y) * X
    
    grad_0 = np.sum(h_y_0) / len(X)
    grad_1 = np.sum(h_y_1) / len(X)
    
    grad = np.array([grad_0, grad_1])
    
    return grad




def update_thetas(X, y, theta_input, alfa):
    
    grads = gradient_single(X, y, theta_input)
    
    for i in range(theta_input.shape[0]):
        theta_input[i] = theta_input[i] - alfa * grads[i]
    
    return theta_input

    

def repeat_single(X, y, theta_input, alfa, iters):
    
    thetas_new = update_thetas(X, y, theta_input, alfa)
    
    for i in range(iters):
        thetas_new = update_thetas(X, y, theta_input, alfa)
        
    return thetas_new

final_thetas = repeat_single(X_, y_, thetas_single, 0.01, 1000)

final_vals = final_thetas[0] + final_thetas[1] * X_



plt.scatter(X_, y_, c='b', label='values x and y')
plt.plot(X_, final_vals, c='r' , label='RL')
plt.title('Best RL')
plt.legend();