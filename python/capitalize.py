#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = []
    x = 0
    to_upp = False
    for c in s:
        if x==0:
            to_upp = True
        elif s[x-1]==" ":
            to_upp = True
        else:
            to_upp = False
        
        if to_upp:
            result.append(c.upper())
        else:
            result.append(c)
        
        x += 1
        
    return "".join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
