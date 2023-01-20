#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    """
    n = towers
    m = towers's height
    input:
    2
    2 2
    1 4
    n m => expected
    2 2 => 2
    1 4 => 1
    """
    # si torre1 y torre2 altura es 6, player1 quita 5 de torre1, luego player2 quita 5 de torre2, gana p2
    # si torre1, torre2, torre3 altura es 6, player1 quita 5, luego player2, luego player1, gana p1
    # entonces: si n torres es par gana p2 o altura de torre es 1
    if n%2==0 or m==1:
        return 2
    else:
        return 1
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

