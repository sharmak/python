# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:12:11 2014

@author: kishor
"""
import numpy as np
from copy import deepcopy
def mat_mult(ML):
    if len(ML) == 1:
        return 1, (ML[0,0] * ML[0,1],)
    if len(ML) == 2:
        return ML[0,0] * ML[0,1] * ML[1,1], (ML[0,0], ML[1,1],)
    for i in xrange(1, len(ML)):
         ML1 = deepcopy(ML)
         s1, s2 = np.vsplit(ML1,[i,])
         print "s1=", s1
         print "s2=", s2
         if len(s1) > 1:
             count1, rem1 = mat_mult(s1)
         if len(s2) > 1:
             count2, rem2 = mat_mult(s2)
    
if __name__ == '__main__':
    ML = np.array([50,20,20,1,1,10,10,100])
    ML = ML.reshape(len(ML)/2.0, 2)
    mat_mult(ML)