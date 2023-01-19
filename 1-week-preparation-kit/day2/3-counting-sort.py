#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    """
    print(arr)
    input: 100
    63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33
    expected:
    0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2
    """
    # size = len(arr)
    size = 100
    result = [0] * size
    # print(result)
    i=0
    while i < len(arr):
        # print("i:", i)
        # print("arr[i]: ", arr[i])
        # print("result[arr[i]]: ", result[arr[i]])
        result[arr[i]] += 1
        i+=1
    # print("result:", result)
    # print("expected: 11 4 11 8 10 12 10 10 12 10 11 8 7 8 8 9 9 15 13 14 15 9 9 11 11 11 14 9 8 15 11 5 14 10 9 9 8 18 6 7 12 7 14 7 6 18 15 13 11 8 9 8 9 17 10 10 8 12 14 4 13 6 15 12 13 6 7 12 3 11 7 7 8 10 12 13 9 6 11 9 3 12 14 6 10 7 12 7 11 7 8 8 13 8 7 10 12 12 13 9")
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

