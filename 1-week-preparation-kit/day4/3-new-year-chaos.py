#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    # print("q", q)
    max_ops=2
    size=len(q)
    bribes=0
    q_sorted = sorted(q)
    while q != q_sorted: # mientras no este ordenado
        for x in range(size): # iteramos cuantas veces sea necesario
            
            moves = q[x] - q_sorted[x] # restamos cada item con el ordenado
            if moves>max_ops: # verificamos si es mayor a 2 movimientos
                print("Too chaotic")
                return
            
            next_position = x + 1
            if q[x] != next_position: # si es diferente al siguiente
                if q[x] > q[x+1]: # si es mayor al siguiente debe intercambiar
                    q[x], q[x+1] = q[x+1], q[x]
                    bribes += 1
    
    print(bribes)
    return

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

