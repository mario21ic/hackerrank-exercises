#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
"""
input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
expected:
19
"""
def hourglassSum(arr):
    # Write your code here
    # print("arr", arr)
    columns = len(arr)-1
    rows = len(arr[0])-1
    x=0
    hourglasses = []
    while x<=rows-2:
        y=0
        # hourglass = []
        while y<=columns-2:
            # print(f"x={x} y={y}")
            # print("arr[x][y]: ", arr[x][y])
            hourglassSum = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            # print("to sum: ", arr[x][y], arr[x][y+1], arr[x][y+2], arr[x+1][y+1], arr[x+2][y], arr[x+2][y+1], arr[x+2][y+2])
            # print("## hourglass:", hourglassSum)
            hourglasses.append(hourglassSum)
            y+=1
            
        # print(f"x={x}")
        # print("arr[x]: ", arr[x])
        x+=1
    # print("hourglasses:", hourglasses)
    return max(hourglasses)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

