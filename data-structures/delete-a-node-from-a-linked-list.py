#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'deleteNode' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
"""
input:
8 # position to remove
20
6
2
19
7
4
15
9
3
expected:
20 6 2 7 4 15 9
"""

def deleteNode(llist, position):
    # Write your code here
    # print("llist:", llist) # SinglyLinkedListNode -> head node
    # print("position:", position) # 3
    
    if position!=0:
        current=llist # head node
        end=False
        x=1
        while end==False:
            # print("data", current.data)
            if x==position:
                # print("## Siguiente se eliminara")
                # print("x: ", x)
                node_next_next = current.next.next
                # print("debemos usar el", node_next_next.data)
                current.next = node_next_next
            if current.next!=None:
                # print("next")
                current = current.next # move to next node
            else:
                end=True
            x+=1
    else:
        llist = llist.next
    return llist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()

