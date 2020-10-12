#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:21:16 2020

@author: oem
"""

import numpy as np

def softmax(W,X,b):
    z = np.exp(np.dot(W,X)+b)
    return z/np.sum(z)


W = np.array([0.1,0.2,0.6])
X = np.array([0.2,0.1,0.3])
b=1.5


print(softmax(W,X,b))

W = np.array([[1,2,3],[2,3,8],[1,5,7]])

print(softmax(W,X,b))