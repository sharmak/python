# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 20:12:36 2014

@author: kishor
"""
from copy import deepcopy
def knapsack_without_rep(w, v, BAG, OUT):
    print w, v, BAG, OUT
    if len(w) == 0:
        return OUT
    if len(v) == 0:
        return OUT
    if BAG <= 0:
        return OUT
        
    w1 = deepcopy(w)
    wt = w1.pop()
    v1 = deepcopy(v)
    value = v1.pop()
    if BAG - wt < 0:
        return OUT
    k1 = knapsack_without_rep(w1, v1, BAG-wt, OUT+value)
    
    w2 = deepcopy(w)
    v2 = deepcopy(v)
    w2.pop()
    v2.pop()
    if BAG - wt < 0:
        return OUT
    k2 = knapsack_without_rep(w2, v2, BAG, OUT)
    
    return max(k1, k2)
    
def knapsack_with_rep(w, v, BAG, OUT):
    print w, v, BAG, OUT
    if len(w) == 0 or len(v) == 0:
        return OUT
    if BAG <= 0:
        return OUT
    w1 = deepcopy(w)
    v1 = deepcopy(v)
    wt = w1.pop()
    val = v1.pop()
    if BAG - wt < 0:
        return OUT
    k1 = knapsack_with_rep(w, v, BAG-wt, OUT+val)
    
    w2 = deepcopy(w)
    v2 = deepcopy(v)
    w2.pop()
    v2.pop()
    if BAG - wt < 0:
        return OUT
    k2 = knapsack_with_rep(w2, v2, BAG, OUT)
    return max(k1, k2)
    
if __name__ == '__main__':
     #print knapsack_without_rep([3,4,7,8,9], [4,5,10,11,13], 17, 0)  
     #print knapsack_without_rep([1,5,3,4], [15,10,9,5],8,0)
     #print knapsack_without_rep([3,4], [9,5],2,0)
     print knapsack_with_rep([6,3,4,2], [30,14,16,9], 10, 0)
     print knapsack_without_rep([6,3,4,2],[30,14,16,9], 10, 0)