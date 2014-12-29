# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 06:01:55 2014

@author: kishor
"""

# 8 queen problem
# Place queens on 8x8 chess board
N= 7
OUTPUT = list()
import numpy as np
def is_queen_solution(n, k):
    return n == k
def generate_queen_candidate(a, n, k):
    BOARD = np.zeros(N*N).reshape((N,N))
    for row in a:
        # mark the row 
        BOARD[row[0],:] = 1
        # mark the column
        BOARD[:, row[1]] = 1
        row_val = row[0]
        col_val = row[1]
        # mark the diagonal
        i, j = row_val, col_val
        while i < N and  j < N:
            #print i, j
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
            # ith queen must be ith row
            # len(a) == row is quiet import as it reduces the 
            # the search space from 64^8 to 8^8
            if BOARD[row, col] == 0 and len(a) == row:
                candidates.append((row, col))
    return candidates

from copy import deepcopy
def print_queen_solution(a):
    #print("OUTPUT")
    print(a)
    a_copy = deepcopy(sorted(a))
    #if a_copy not in OUTPUT:
    OUTPUT.append(a_copy)
def queen_backtrack(a, n, k):
    if is_queen_solution(n, k):
        print_queen_solution(a)
    else:
        k = k + 1
        candidates = generate_queen_candidate(a,n, k)
        for c in candidates:
            a.append(c)
            queen_backtrack(a, n, k)
            a.remove(c)
a = list(range(N))
queen_backtrack(list(), N, 0)
print len(OUTPUT)
#print(OUTPUT[0])
#print len(set(OUTPUT))