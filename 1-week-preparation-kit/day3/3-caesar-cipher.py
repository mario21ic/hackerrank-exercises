#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

"""
input:
11
middle-Outz
2
expected:
okffng-Qwvb
# case 2:
www.abc.xy + 87 => fff.jkl.gh
"""
def caesarCipher(s, k):
    # print("s", s) # middle-Outz
    # print("k", k) # 2
    if k>=26:
        k = k%26
    # print("k", k)

    
    alf_min = "abcdefghijklmnopqrstuvwxyz"
    alf_min_new = ""
    x=0
    position=0
    for a in alf_min:
        position = x+k
        if position>=26:
            position -= 26
        alf_min_new += alf_min[position]
        x+=1
    # print("min new:",alf_min_new)
    
    alf_may = alf_min.upper()
    alf_may_new = alf_min_new.upper()
    # print("may new:",alf_may_new)
    
    result = ""
    for c in s:
        # print("c", c)
        c_ascii = ord(c)
        # print("c_ascii",c_ascii)
        
        if (c_ascii>=97 and c_ascii<=122):
            result += alf_min_new[alf_min.index(c)]
        
        elif (c_ascii>=65 and c_ascii<=90):  
            result += alf_may_new[alf_may.index(c)]
        
        else:
            result += c
        
        # print("result", result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

