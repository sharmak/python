# -*- coding: utf-8 -*-
"""
Created on Sat Nov 08 23:18:57 2014

@author: admin
"""
def combination(a):
    for i in xrange(pow(2, len(a))):
        # Generate bits for i        
        bits = map(int, list(bin(i)[2:]))
        if len(bits) < len(a):
            diff = len(a) - len(bits)
            z = [0 for i in xrange(diff)]
            bits = z + bits
        # For all set bits print the value
        value = list()
        for index, j in enumerate(bits):
            if j == 1:
                value.append(a[index])
        print value
        
def combination_recursive(A, start, end):
    if start == end:
        A[start] = 0
        print A
        A[start] = 1 
        print A
    else:
        A[start] = 0
        combination_recursive(A, start+1, end)
        A[start] = 1
        combination_recursive(A, start+1, end)
# Permuations    
COUNT = 0        
def permutation(A, ar):
    if len(A) == 1:
        global COUNT        
        #print ar + A
        COUNT += 1
    else:
        for i, value in enumerate(A):
            ar.append(value)
            permutation(A[:i]+A[i+1:], ar)
            ar.pop()
            
        
        
import numpy as np   
import scipy 
if __name__ == '__main__':
    o = list()
    l = range(1, np.random.randint(2, 10))
    permutation(l, o)
    #print l
    if COUNT != int(scipy.misc.factorial(len(l))):
        raise ValueError("Failed")
    #print COUNT
    print combination_recursive(list(np.zeros(4 )), 0, 3)