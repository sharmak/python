# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 19:44:46 2014

@author: kishor
"""
def LIS_Rec(L):
    #print L
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return 1
    top_ele = L[-1]
    L.remove(L[-1])
    out = list()
    rev_L = L[::-1]
    #print top_ele    
    for i, ele in enumerate(rev_L):
        index = L.index(ele)
        new_list = L[:index+1]
        if ele < top_ele:   
            out.append(1+LIS_Rec(new_list))
        else:
            out.append(LIS_Rec(new_list))
    return max(out)
import numpy as np
def LIS_Dp(L):
    M = np.zeros(len(L)*len(L))
    M = M.reshape(len(L), len(L))
    for i in xrange(len(L)):
        M[i,i] = 1
    for SC in xrange(1, len(L)):
        for i, j in zip(range(0, len(L)), range(SC, len(L))):
            M[i,j] = M[i, j-1]            
            #print i, j, L[i], L[j], L[j-1]            
            if L[j-1] < L[j]:
                M[i,j] = M[i,j]+1

    #print M
    return M[0, len(L)-1]            
        
if __name__ == '__main__':
    print LIS_Dp([9,8,1,2])
    print LIS_Dp([0, 22, 9, 33, 21, 50, 41, 60, 80 ])
    print LIS_Rec([9,8,1,2])
    print LIS_Rec([0, 22, 9, 33, 21, 50, 41, 60, 80 ])