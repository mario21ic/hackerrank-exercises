#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #print(arr) # [-4, 3, -9, 0, 4, 1]
    arr_len = len(arr)
    n_positives = 0
    n_negatives = 0
    n_zeros = 0
    for n in arr:
        # print(n)
        if n == 0:
            n_zeros += 1
        if n >= 1:
            n_positives +=1
        if n < 0:
            n_negatives += 1

    print("{:.6f}".format(round(n_positives/arr_len, 6)))
    print("{:.6f}".format(round(n_negatives/arr_len, 6)))
    print("{:.6f}".format(round(n_zeros/arr_len, 6)))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

