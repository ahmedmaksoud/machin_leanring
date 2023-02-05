# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:58:10 2023

@author: 459
"""


import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

data_single = np.genfromtxt('RegData.csv', delimiter=',')

X_fe = data_single[:,0].reshape(-1,1)
Y_fe = data_single[:,1].reshape(-1,1)

thetas_single = np.zeros(2)


# let we start theta 0 and  theta 1 with zero
thetas_single = np.zeros(2)


def predict_single(X, theta_input):
    #p = theta0 + theta1 * x
    predicts = thetas_single[0] + thetas_single[1] * X
    return predicts
# x
c = predict_single(X_fe, thetas_single)

print ("predict_single ", c)


def cost_single(X, Y, theta_input):
     pridects = predict_single(X, theta_input)  #  theta0 + theta1 * x
     h_y = (pridects - Y) ** 2 # (theta0 + theta1 * x - Y ) ^ 2 
     j = (1 / 2 * len(X) )  * np.sum(h_y)
     
     #h_y = (pridects - Y)**2
     #j = np.sum(h_y) / (2* len(X))
    
     return j;
cost_single_p = cost_single(X_fe, Y_fe,thetas_single ) 
print ("cost_single ",cost_single_p  )


def gradient_single(X, Y, theta_input):
    
    predicts = predict_single(X, theta_input)
    
    h_y_0 =( predicts - Y)  * 1
    h_y_1 = (predicts - Y) * X
    
    grad_0 = 1 /  len(X) * np.sum(h_y_0) 
    grad_1 = 1 /  len(X) * np.sum(h_y_1)  
    #grad_0 = np.sum(h_y_0) / len(X)
    #grad_1 = np.sum(h_y_1) / len(X)
    
    grad = np.array([grad_0, grad_1])
    return grad

gradient_single_p = gradient_single(X_fe, Y_fe, thetas_single)

print ("gradient_single ",gradient_single_p  )    
    


def update_thetas(X, y, theta_input, alfa):
    
    grads = gradient_single(X, y, theta_input)
    
    for i in range(theta_input.shape[0]):
        theta_input[i] = theta_input[i] - alfa * grads[i]
    
    return theta_input

update_thetas_p = update_thetas(X_fe, Y_fe, thetas_single, 0.001) 
  
print ("update_thetas ",update_thetas_p  )      
     
 
def repeat_single(X, y, theta_input, alfa, iters):
    
    thetas_new = update_thetas(X, y, theta_input, alfa)
    
    for i in range(iters):
        thetas_new = update_thetas(X, y, theta_input, alfa)
        
    return thetas_new

final_thetas = repeat_single(X_fe, Y_fe, thetas_single, 0.01, 1000)
print ("final_thetas" , final_thetas)


final_vals = final_thetas[0] + final_thetas[1] * X_fe
print ("final_vals" , final_vals)



plt.scatter(X_fe, Y_fe, c='b', label='values x and y')
plt.plot(X_fe, final_vals, c='r' , label='RL')
plt.title('Best RL')
plt.legend();   