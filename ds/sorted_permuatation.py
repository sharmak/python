# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 06:01:26 2014

@author: kishor
"""

# Sorted Permuataion problem
def is_perm_solution(n, k):
    return n == k

def generate_perm_candidates(n, k, a, data):
    candidates = list()
    for ele in data:
        if ele not in a:
            candidates.append(ele)
    return sorted(candidates)

def print_perm_solution(a, data):
    print a
    
def permutations(a, n, k, data):
    if is_perm_solution(n, k):
        print_perm_solution(a, data)
    else:
        k = k + 1
        candidates = generate_perm_candidates(n, k, a, data)
        for c in candidates:
            a[k-1] = c
            permutations(a, n, k, data)
            a[k-1] = -1

data = [1, 2, 3]
a = [-1, -1, -1]
permutations(sorted(a), 3, 0, data)