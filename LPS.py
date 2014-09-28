# -*- coding: utf-8 -*-
"""
Longest Palidromic Sequence
Created on Sun Sep 28 14:31:24 2014

@author: Kishor
"""
def LPS_Rec(s):
    #print s
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0
    if len(s) == 2 and s[0] == s[1]:
        return 2
    if s[0] == s[-1]:
        return 2 + LPS_Rec(s[1:-1])

    return max(LPS_Rec(s[1:]), LPS_Rec(s[:-1]))
import numpy as np
def LPS_DP(s):
    M = np.zeros(len(s)*len(s))
    M = M.reshape(len(s), len(s))

    # M[i,j] denotes the LPS from i to j
    # Set 1 on the diagonal as M[i,i] is 1
    for i in xrange(len(M)):
        M[i,i] = 1
    
    # M[i, j] = max {M[i+1, j], M[i, j-1]}
    # if s[i] == s[j]  M[i+1, j-1] + 2
    for start_col in xrange(1, len(s)):
        for i, j in zip(range(0,len(s)), range(start_col, len(s))):
            print i, j            
            if s[i] == s[j]:
                M[i,j] = M[i+1,j-1] + 2
            else:
                M[i,j] = max(M[i+1, j], M[i, j-1])
    print M
    
        
    
if __name__ == '__main__':
    print LPS_DP('GEEKFORGEEKS')
    print LPS_Rec("BBABCBCAB")
    print LPS_Rec("GEEKFORGEEKS")