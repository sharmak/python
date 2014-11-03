# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 01:07:31 2014

@author: kishor
"""
import numpy as np

# Print matrix in spiral order
def print_spiral(M):
    rows = len(M)
    cols = 0
    try:
        cols = len(M[0])
    except:
        pass
    if rows <= 1 or cols <= 1:
        print M
    else:
        # First row
        print M[0]
        # Last column
        print M[1:,-1]
        # Last row
        print list(reversed(M[-1,1:-1]))
        # First column
        print list(reversed(M[1:,0]))
        
        # Recursively calll the same function
        # on inner matrix
        print_spiral(M[1:-1,1:-1])
        
if __name__ == '__main__':
    r = np.random.randint(1,50)    
    M = np.arange(r*r)
    M = M.reshape(r,r)
    print M
    print_spiral(M)