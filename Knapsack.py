# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 20:12:36 2014

@author: kishor
"""
from copy import deepcopy
def knapsack(w, v, BAG, OUT):
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

    k1 = knapsack(w1, v1, BAG-wt, OUT+value)
    
    w2 = deepcopy(w)
    v2 = deepcopy(v)
    w2.pop()
    v2.pop()
    k2 = knapsack(w2, v2, BAG, OUT)
    
    return max(k1, k2)
    
if __name__ == '__main__':
     print knapsack([3,4,7,8,9], [4,5,10,11,13], 17, 0)  
     #print knapsack([1,5,3,4], [15,10,9,5],8,0)
     #print knapsack([3,4], [9,5],2,0)