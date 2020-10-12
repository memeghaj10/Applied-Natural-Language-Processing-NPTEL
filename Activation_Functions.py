# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def sigmoid(X,W,b):
    return 1.0/(1.0+np.exp(-(np.dot(W.T,X)+b)))

def tanh(X,W,b):
    z = np.exp(-(np.dot(W.T,X)+b))
    return (np.exp(z)-np.exp(-z))/(np.exp(z)+np.exp(-z))

def relu(X,W,b):
    x = np.dot(W.T,X)+b
    return np.maximum(x,0)

def softmax(X,W,b):
    z_exp = np.exp(np.dot(W.T,X)+b)
    z_exp_sum = np.sum(z_exp)
    return z_exp/z_exp_sum

W = np.array([0.1,0.2,0.6])
X = np.array([0.2,0.1,0.3])

b=1.5

print(sigmoid(X, W, b))
print(tanh(X,W,b))
print(relu(X,W,b))
print(softmax(X,W,b))

