#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    x = 0
    arr.sort()
    n_items = len(arr)-1
    # print("n_items:", n_items)
    while x <= n_items:
        # print(arr[x])
        if x < n_items:
            min_sum += arr[x]
        if x != 0:
            max_sum += arr[x]
        x += 1
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

