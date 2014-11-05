# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 01:20:03 2014

@author: admin
"""
# Compute no of paths in MXN matrix using recursion
# and dynamic programming
def no_of_path_rec(m, n):
    # OR indicates that we have reached last 
    # row or column there is only one path now. 
    if m == 1 or n == 1:
        return 1
    else:
        return no_of_path_rec(m-1, n) + no_of_path_rec(m, n-1)

import numpy as np
def no_of_path_dp(m, n):
    M = np.zeros((m+1)*(n+1))
    M = M.reshape(m+1, n+1)
    M[1,1] = 1
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if i == 1 and j == 1:
                continue
            M[i,j] = M[i-1, j] + M[i, j-1]
    return M[m, n]
         
    
if __name__ == '__main__':
    print no_of_path_rec(3,3)
    print no_of_path_dp(3, 3)
    