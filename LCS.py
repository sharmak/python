# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:42:42 2014

@author: kishor
Longest Common Sequence
S1  - S U N N Y
S2  - S N O W Y
LCS - S N Y
"""

def LCS_Rec(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    if len_str1 == 0 or len_str2 == 0:
        return 0
    if str1[0] == str2[0]:
        return 1 + LCS_Rec(str1[1:], str2[1:])
    else:
        return max(LCS_Rec(str1[0:], str2[1:]), LCS_Rec(str1[1:], str2[0:]))

if __name__ == '__main__':
    print LCS_Rec("sunny", "snowy")
    print LCS_Rec("acbd", "acbd")
    print LCS_Rec("vnvn", "vn")
    print LCS_Rec("ABCDEF", "CDEFAB")