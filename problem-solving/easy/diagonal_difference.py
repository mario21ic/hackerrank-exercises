#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

"""
input:
3
11 2 4
4 5 6
10 8 -12
"""
def diagonalDifference(arr):
    # Write your code here
    # print(arr) # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    # print(arr) # [[6 8], [-6 9]]
    # print(arr) # [[-1 1 -7 -8], [-10 -8 -5 -2], [0 9 7 -1], [4 4 -2 1]]
    # diag_sum1 = arr[0][0] + arr[1][1] + arr[2][2]
    # diag_sum2 = arr[0][2] + arr[1][1] + arr[2][0]
    
    diag_sum1 = 0
    x_len = len(arr)-1    
    x = 0
    y = 0
    while x <= x_len:
        # print("x", x)
        # print("y", y)
        # print(arr[x][y])
        diag_sum1 += arr[x][y]
        x += 1
        y += 1
    
    # print("inversa")
    diag_sum2 = 0
    x = 0
    y = x_len
    while y >= 0:
        # print("x", x)
        # print("y", y)
        # print(arr[x][y])
        diag_sum2 += arr[x][y]
        x += 1
        y -= 1
        
    return abs(diag_sum1 - diag_sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

