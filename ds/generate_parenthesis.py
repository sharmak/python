# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 00:46:11 2015

@author: kishor
"""
import sys

def score(mystr):
    return mystr.count('(') - mystr.count(')')
    
def generate_solutions(input, output, n):
    input_score = score(input)
    res = list()
    for i in set(input):
        loop_input = input
        loop_output = output        
        loop_input = loop_input.replace(i, '', 1)
        loop_output += i
        output_score = score(loop_output)
        if output_score > n or output_score < 0:
            continue
        else:
            res.append((loop_input, loop_output))
    #print(res)   
    return res
def generate_parenthesis_rec(input, output, n):
    if len(output) == 2*n:
        print(output)
    else:
        pos_sols = generate_solutions(input, output, n)
        for sol in pos_sols:
            generate_parenthesis_rec(sol[0], sol[1],  n)
def generate_parenthesis(n):
    input = '(' * n + ')'*n
    #print(input)
    output = ''
    generate_parenthesis_rec(input, output, n)
if __name__ == '__main__':
    generate_parenthesis(3)