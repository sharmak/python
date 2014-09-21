# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 22:51:29 2014

@author: kishor
"""

"""
Given a value N, if we want to make change for N cents, and 
we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins,
how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, 
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
So output should be 4. 
For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} 
and {5,5}. So the output should be 5.

To understand this, we need handle two cases:
 a) Exclude Nth value
 b) Include Nth value   

"""
from copy import deepcopy
def coins(s, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    if len(s) == 0:
        return 0

    # Case1: exclude nth value
    s1 = deepcopy(s)
    removed_value = s1.pop()
    w1 = coins(s1, n)
    
    # Case 2 include nth value
    s2 = deepcopy(s)
    w2 = coins(s2, n-removed_value)
    return w1 + w2
    
    #
    return ways
if __name__ == '__main__':
    print coins([1,2,3], 4)
    print coins([2,5,3,6], 10)    