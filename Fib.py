# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:25:11 2014

@author: kishor
"""
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
FIB_LOOKUP = dict()
def fib_memoize(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        try:
            fib_n_1 = FIB_LOOKUP[n-1]
        except KeyError:
            fib_n_1 = fib_memoize(n-1)
            FIB_LOOKUP[n-1] = fib_n_1
        try:
            fib_n_2 = FIB_LOOKUP[n-2]
        except:
            fib_n_2 = fib_memoize(n-2)
            FIB_LOOKUP[n-2] = fib_n_2
        return fib_n_1 + fib_n_2


def fib_DP(n):
    fib = [0]*(n+1)
    fib[0] = 0
    fib[1] = 1
    for i in xrange(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
    
def fib_MATRIX(n):
    import numpy as np
    magic_arr = np.array([0,1,1,1])
    magic_arr.resize(2,2)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev = 0
    curr = 1
    for i in xrange(2,n+1):
        res = np.dot(magic_arr, [prev, curr])
        prev = curr
        curr = res[1]
    return curr
        
if __name__ == '__main__':
    n = 10
    print fib_recursive(n)
    print fib_memoize(n)
    print fib_DP(n)
    print fib_MATRIX(n)
