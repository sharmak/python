# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 22:29:40 2014

@author: kishor
"""
import numpy as np
# Add a horizontal and vertial stacking of zeors
# to the cost matrix
def prepare_cost_matrix(MAT):
    row, col = MAT.shape

    horizontal_row = np.zeros(col)
    MAT = np.row_stack((horizontal_row, MAT))
    MAT = np.column_stack((np.zeros(row+1), MAT))
    return MAT

CACHE = dict()
def memoize(fn):
    def wrap_fn(*args, **kwargs):
        try:
            return CACHE[str(args) + str(kwargs)]
        except:
            pass
        out = fn(*args, **kwargs)
        CACHE[str(args)+ str(kwargs)] = out
        return out
    return wrap_fn

@memoize       
def min_cost(MAT, i, j):
    if i == 0 and j == 0:
        return MAT[i, j]
    if i == 0:
        return MAT[i,j] + min_cost(MAT, i, j-1)
    if j == 0:
        return MAT[i, j] + min_cost(MAT, i-1, j)
    row, col = MAT.shape
    return min(MAT[i, j ] + min_cost(MAT, i, j-1),
               MAT[i, j]  + min_cost(MAT, i-1, j),
               MAT[i, j]  + min_cost(MAT, i-1, j-1))
def min_cost_dp(MAT, target_i, target_j):
    COST = np.copy(MAT)
    row, col = COST.shape
    s = 0
    s1 = 0
    for i in xrange(row):
        s += COST[i, 0]        
        COST[i, 0] = s
    for i in xrange(col):
        s1 += COST[0, i]
        COST[0, i] = s1
    for i in xrange(1, row):
        for j in xrange(1, col):
            COST[i, j] = min(COST[i-1, j], COST[i, j-1], COST[i-1,j-1]) \
                            + COST[i, j]            
    return COST[target_i, target_j]
if __name__ == '__main__':
    row, col = 3,3
    a = np.array([1,2,3,4,8,2,1,5,3])
    #a = np.ones(row*col)    
    a.resize(row, col)  
    #a = prepare_cost_matrix(a)
    print a    
    #print min_cost(a,2,2)
    print min_cost_dp(a,2,2)