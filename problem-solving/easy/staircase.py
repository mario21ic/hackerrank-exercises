#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    x = 1
    while x<=n:
        # print(x)
        print(" "*(n-x) + "#"*x)
        x += 1

if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)

