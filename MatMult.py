# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:12:11 2014

@author: kishor
"""
import numpy as np
from copy import deepcopy
def mat_mult(ML):
    # 1 element means no matrix at all 
    # so return 0
    if len(ML) == 1:
        return 0
    # 2 elements mean one matrix so
    # you can't multiply at all
    if len(ML) == 2:
        return 0
    min = 123434243
    for i in xrange(2, len(ML)):
         ML1 = deepcopy(ML)
         s1 = ML1[:i]
         s2 = ML1[i-1:]
         #print "s1 = ",s1
         #print "s2 = ", s2
         count_s1 = mat_mult(s1)
         count_s2 = mat_mult(s2)
         count = count_s1 + count_s2 + (s1[0]  * s1[-1] * s2[-1])
         if count < min:
             min = count
         #print count         
    return min
    
if __name__ == '__main__':
    ML = [10, 20, 30, 40, 30]
    print mat_mult(ML)
    ML = [10, 20, 30]  
    print mat_mult(ML)
    ML = [40, 20, 30,10, 30]    
    print mat_mult(ML)
    