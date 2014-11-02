# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 23:23:46 2014

@author: kishor
"""

# Given a sorted matrix by row and column search for an element
# Input:   { {10, 20, 30, 40},
#           {15, 25, 35, 45},
#           {27, 29, 37, 48},
#           {32, 33, 39, 50},
#        };
# Solutions:
# 1. We can search linearly for an element which is O(n^2)
# 2. We can do binary search over each row to find the element
#    O(n*Log(n))
# 3. We take upper right element if se element is less than upper right 
#    element then we search a[R][C-1] matrix otherwise we can search in 
#    a[R+1][C] matrix 
import numpy as np

def sorted_mat_search(M, se):
    if np.size(M) == 0:
        return False
    if np.size(M) == 1:
        if M[0,0] != se:
            return False
        else:
            return True
    else:
        cols = len(M[0])
        if M[0, cols-1] == se:
            return True
        elif M[0, cols-1] < se:
            return sorted_mat_search(M[1:,], se)
        elif M[0, cols-1] > se:
            return sorted_mat_search(M[:,0:cols-1], se)
        else:
            raise ValueError("Not Possible")

# Given sorted matrix by rows and column print all the elements in 
# sorted order
# This problem can be viewed as merging K sorted arrays
#  Use merge (used in merge sort) to merge the elements
#     Instead of finding minimum of two elements we have find mininum
#     of n-elements while merging the elements. We can either use
#     use Heap to keep track of the minimum element.
from heapq import *
class MatrixElement(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index
    def __lt__(self, other):
        return self.value < other.value
    def __str__(self):
        return "%d %s" %(self.value, str(self.index))
def sort_sorted_matrix(M):
    rows = len(M)
    H = list()
    if rows == 0:
        raise ValueError("Undefined Matrix")
    for index, value in enumerate(M[0]):
        o = MatrixElement(value, (0, index))
        heappush(H, o)
    S = list()
    while (len(H) > 0):
        o = heappop(H)
        S.append(o.value)
        if o.index[0] < rows-1:
            new_index = (o.index[0]+1, o.index[1])
            #print new_index
            element = M[new_index[0], new_index[1]]
            new_obj = MatrixElement(element, new_index)
            heappush(H,new_obj)
    print S
    
    
              
if __name__ == '__main__':
    r = np.random.randint(1,50)
    M = np.arange(r*r)
    M  = M.reshape(r,r)
    print M    
    #print sorted_mat_search(M, r)
    sort_sorted_matrix(M)    