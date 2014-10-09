# -*- coding: utf-8 -*-
"""
Compute Bionomial cofficents
Created on Sun Sep 28 11:27:25 2014

@author: admin
"""
from copy import deepcopy
import numpy as np
def BC_Rec(n):
    if n == 2:
        return [1,1]
    bc_prev= BC_Rec(n-1)
    bc_prev_copy = deepcopy(bc_prev)
    bc_prev.insert(0, 0)
    bc_prev_copy.append(0)
    return list(np.add(bc_prev, bc_prev_copy))

def BC_dp(n):
    
    if n == 2:
        return [1,1]
    B = list()
    B.append([1,1])
    for i in xrange(2, n):
        bc_prev = B.pop()
        bc_prev_copy = deepcopy(bc_prev)
        bc_prev.insert(0, 0)
        bc_prev_copy.append(0)
        B.append(list(np.add(bc_prev, bc_prev_copy)))
    return B[0]        
if __name__ == '__main__':
    print BC_Rec(5)
    print BC_dp(5)    