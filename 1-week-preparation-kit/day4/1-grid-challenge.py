#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
"""
input:
1
5
eabcd
fghij
olkmn
trpqs
xywuv
expected: YES

mpxz
abcd
wlmf
NO
"""
def gridChallenge(grid):
    # print("="*5)
    # print("grid:", grid)
    new_grid = []
    for row in grid:
        r_sorted = "".join(sorted(row))
        new_grid.append(r_sorted)
    # print("new_grid", new_grid)
    
    result = "NO"
    x=0
    size=len(new_grid)
    # print("len(new_grid[0]", len(new_grid[0]))
    # print("size", size)
    while x < len(new_grid[0]): # len of horizontal item mpxz
        c_prev = 97
        y=0
        while y < size: # len of vertical items
            # print("y=%s x=%s" % (y, x))
            item = new_grid[y][x]
            # print("c_prev", c_prev)
            # print("item", ord(item))
            if ord(item)>=c_prev:
                result = "YES"
            else:
                return "NO"
            c_prev = ord(item)
            y+=1
        x+=1
    # print("result:", result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

