# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 22:10:08 2014

@author: admin
"""
def rod_rec(size, values):
    if size == 1:
        return values[0]
    else:
        max_value = -1
        n= len(values)
        for i in xrange(1, len(values)):
            new_value = rod_rec(n-i, values[:-1*i]) + rod_rec(i,values[:i])
            if new_value > max_value:
                max_value = new_value
        return max(max_value, values[-1])

import numpy as np
def rod_dp(size, values):
    M = np.zeros(size+1)
    for i in xrange(1, size+1):
        out = list()
        out.append(values[i-1])
        for j in xrange(1, i+1):
            out.append(M[i-j]+ M[j])
        M[i] = max(out)
    return M[-1]
            
if __name__ == '__main__':
    #print rod_rec(8, [1, 5, 8, 9, 10, 17, 17, 20])
    print rod_dp(8, [1, 5, 8, 9, 10, 17, 17, 20])