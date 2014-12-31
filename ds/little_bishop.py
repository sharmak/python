# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 08:01:24 2014

@author: kishor
"""
COUNT = 0
N = 4
import numpy as np
OUTPUT = list()
from copy import deepcopy
def is_bishop_solution(n, k):
    return n == k
def print_bishop_solution(a, n, k):
    global COUNT
    #print(a)
    a_copy = deepcopy(a)
    a_copy = sorted(a_copy)
    if a_copy not in OUTPUT:
        OUTPUT.append(a_copy)
    COUNT += 1
def generate_bishop_candidate(a, n, k):
    BOARD = np.zeros(N*N).reshape((N,N))
    for partial_sol_row in a:
        row_val = partial_sol_row[0]
        col_val = partial_sol_row[1]
        
        # mark the diagonal
        i, j = row_val, col_val
        while i < N and  j < N:
            BOARD[i, j] = 1
            i = i + 1
            j = j + 1
        i, j = row_val, col_val
        while i >= 0 and  j >= 0:
            #print i, j
            BOARD[i, j] = 1
            i = i - 1
            j = j - 1   
        i, j = row_val, col_val
        while i >= 0 and j < N:
            BOARD[i, j] = 1
            i = i -1
            j = j + 1
        
        i, j = row_val, col_val
        while i < N and j >= 0:
            BOARD[i, j] = 1
            i = i + 1
            j = j - 1
        
    candidates = list()
    #print BOARD
    for row in xrange(BOARD.shape[0]):
        for col in xrange(BOARD.shape[1]):
            if BOARD[row, col] == 0 :
                candidates.append((row, col))
  
    new_candidates= list()
    if len(a) >= 1:
        last_point = a[-1]
        for c in candidates:
            if c[0] > last_point[0]:
                    new_candidates.append(c)
            if c[0] == last_point[0] and c[1] > last_point[1]:
                    new_candidates.append(c)
    else:
        new_candidates = candidates
    return new_candidates
    
def bishop_backtrack(a, n, k):
    if (is_bishop_solution(n, k)):
        print_bishop_solution(a, n, k)
    else:
        k = k + 1
        candidates = generate_bishop_candidate(a, n, k)
        for c in candidates:
            a.append(c)
            bishop_backtrack(a, n, k)
            a.remove(c)
            
if __name__ == '__main__':
    bishop_backtrack(list(), 2, 0) 
    print COUNT
    print len(OUTPUT)