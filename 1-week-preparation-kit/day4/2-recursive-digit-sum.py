#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def getP(n, k):
    result = ""
    x=0
    while x<=int(k):
        result+=str(n)
    return result

def superDigit(n, k):
    # print("n", n)
    # print("type n", type(n))
    # print("k", k)
    # print("type k", type(k))
    
    def sumDigits(number):
        # print("number", number)
        total = 0
        for n in number:
            total += int(n)
        total = str(total)
        # print("total:", total)
        if len(total)==1:
            return total
        return sumDigits(total)
    
    # p = getP(n, k)
    # p = str(n)*k
    p = str(sumDigits(n)*k) # optimizacion
    return sumDigits(p)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

