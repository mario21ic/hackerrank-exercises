#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # print("s:", s)
    hour = s[:2]
    min_seg = s[2:8]
    indicator = s[-2:]
    result = 0
    if hour=="12" and indicator=="AM":
        result =  "00" + min_seg
    elif hour=="12" and indicator=="PM":
        result =  "12" + min_seg
    elif indicator=="PM":
        result = str(int(hour) + 12) + min_seg
    else:
        result = hour + min_seg
    # print("result",result)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

