# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 12:45:45 2014

@author: admin
"""

from copy import deepcopy
def set_union():
    a = [1,2,3,4,5,6,7,8]
    p = deepcopy(a)
    for i in xrange(len(a)):    
        p[i] = a[i]
    def union(i, j):
        print i, j
        if p[i-1] != i:
            return union(p[i-1], j)
        if p[j-1] != j:
            return union(i, p[j-1])
        p[i-1] = j
            
    union(1,2)
    print a
    print p    
    union(3,4)
    union(5,6)
    union(7,8)
    print a
    print p
    union(1,4)
    union(1,8)
    print a
    print p
if __name__ == '__main__':
    set_union()    