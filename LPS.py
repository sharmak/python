# -*- coding: utf-8 -*-
"""
Longest Palidromic Sequence
Created on Sun Sep 28 14:31:24 2014

@author: Kishor
"""
def LPS_Rec(s):
    #print s
    if len(s) == 1:
        return 1
    if len(s) == 0:
        return 0
    if len(s) == 2 and s[0] == s[1]:
        return 2
    if s[0] == s[-1]:
        return 2 + LPS_Rec(s[1:-1])

    return max(LPS_Rec(s[1:]), LPS_Rec(s[:-1]))
if __name__ == '__main__':
    print LPS_Rec("BBABCBCAB")
    print LPS_Rec("GEEKFORGEEKS")