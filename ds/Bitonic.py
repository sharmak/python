# -*- coding: utf-8 -*-
"""
Created on Thu Oct 02 23:37:47 2014

@author: admin
"""
import numpy as np
from copy import deepcopy
def bitonic(L):
    # LIS -> Longest increasing sequence ending at i
    LIS = list(np.ones(len(L), dtype="int"))
    for i in xrange(1, len(L)):
        for j in xrange(0, i):
            if L[i] > L[j] and LIS[i] <= LIS[j] + 1:
                LIS[i] = LIS[j] + 1
    print L
    print LIS
    RL = deepcopy(L[::-1])
    # Longest decreasing sequence starting at i
    LDS = list(np.ones(len(L), dtype="int"))
    for i in xrange(1, len(RL)):
        for j in xrange(0, i):
            if RL[i] > RL[j] and LDS[i] <= LDS[j] + 1:
                LDS[i] = LDS[j] + 1
    max = 0
    for i, j in zip(LIS, LDS):
        if i+j-1 > max:
            max = i+j-1
    return max
    
if __name__ == '__main__':
    print bitonic([80, 60, 30, 40, 20, 10])