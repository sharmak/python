# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 23:40:36 2014

@author: kishor
"""

import numpy as np
from copy import deepcopy

def MSIS_dp(L):
    M = deepcopy(L)
    for i in xrange(1, len(L)):
        for j in xrange(0,i):
            if L[i] > L[j] and M[i] <= M[j] + L[i]:
                M[i] = M[j] + L[i]
    return max(M)
                
if __name__ == '__main__':
    print MSIS_rec([1, 101, 2,3,108])#100, 4, 5])
    #print MSIS_dp([1, 101, 2, 3, 100, 4, 5])