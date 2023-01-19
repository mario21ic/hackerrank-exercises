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

def diagonalDifference(arr):
    # print(arr)
    # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    x = 0
    y = len(arr)-1
    sum_a = 0
    sum_b = 0
    for a in arr:
        sum_a += a[x]
        x+=1
        sum_b += a[y]
        y-=1
    # print(sum_a)
    # print(sum_b)
    return abs(sum_a - sum_b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

