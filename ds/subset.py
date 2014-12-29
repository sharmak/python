# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 06:00:54 2014

@author: kishor
"""

# Subset problem
# Given a set find all the subset of the given set
# e.g. {1,2,3} => {{1},{2}, {3}, {1,2}, {1,3} {2,3}, {1,2,3}, {}}

# Solve the problem using backtracking
def is_subset_solution(n, k):
    return n == k 
def generate_subset_candidates(n, k):
    # Kth element can be either present or not
    # present in the subset solution
    return [True, False]
def process_subset_solution(a, data):
    values = list()
    for i in xrange(len(a)):
        if a[i]:
            values.append(data[i])
    print(values)
    
def subset_backtrack(a, n, k, data):
    #print(n, k)
    if is_subset_solution(n, k):
        process_subset_solution(a, data)
    else:
        k = k + 1
        #print(k)
        #print(n)
        candidates = generate_subset_candidates(n, k)
        for c in candidates:
            a[k-1] = c
            subset_backtrack(a, n, k, data)
subset_backtrack([False,False,False], 3, 0, [1,2,3])
    