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
    minimum=0
    maximum=0
    sum_all=0
    for n in arr:
        sum_all += n
        if (minimum==0) or (n < minimum):
            minimum = n
        if n > maximum:
            maximum = n
    # print(maximum)
    # print(minimum)
    sum_min=sum_all - maximum
    sum_max=sum_all - minimum
    print(sum_min, sum_max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

