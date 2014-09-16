# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:42:42 2014

@author: kishor
Longest Common Sequence
S1  - S U N N Y
S2  - S N O W Y
LCS - S N Y
"""
LCS_LOOKUP = dict()
def LCS_Meomized(str1, str2):
    try:
        return LCS_LOOKUP[(str1, str2)]
    except KeyError:
        pass
    len_str1 = len(str1)
    len_str2 = len(str2)
    
    if len_str1 == 0 or len_str2 == 0:
        res = 0
        LCS_LOOKUP[(str1, str2)] = res
        return res
    if str1[0] == str2[0]:
        res = 1 + LCS_Meomized(str1[1:], str2[1:])
        LCS_LOOKUP[(str1, str2)] = res
        return res
    else:
        res1 = LCS_Meomized(str1[0:], str2[1:])
        res2 = LCS_Meomized(str1[1:], str2[0:])
        res =  max(res1, res2)
        LCS_LOOKUP[(str1, str2)] = res
        return res
        
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
    print "x" * 80
    
    print LCS_Meomized("sunny", "snowy")
    print LCS_Meomized("acbd", "acbd")
    print LCS_Meomized("vnvn", "vn")
    print LCS_Meomized("ABCDEF", "CDEFAB")