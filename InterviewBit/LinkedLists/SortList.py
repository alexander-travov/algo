"""
Sort List
=========

Sort a linked list in O(n log n) time using constant space complexity.
"""

from __future__ import print_function
from random import randrange
from linked_list import Node


def partition(l):
    # Lomuto's partition with randomized pivot
    # and self-balancing of equal elements.
    pivot = l.nth(randrange(len(l))).val
    heads = [None, None]
    tails = [None, None]
    lens = [0, 0]
    
    node = l
    while node is not None:
        if node.val < pivot or node.val == pivot and lens[0] < lens[1]:
            ind = 0
        else:
            ind = 1

        if heads[ind] is None:
            heads[ind] = node

        if tails[ind] is not None:
            tails[ind].next = node
        tails[ind] = node
        node = node.next
        tails[ind].next = None
        lens[ind] += 1

    return heads


def qsort(l):
    if l is None or l.next is None:
        return l
    head, tail = partition(l)
    head = qsort(head)
    tail = qsort(tail)
    if head is not None:
        head.last.next = tail
        return head
    else:
        return tail


l = Node.from_iterable([2, 2, 2, 1, 2, 2, 8, 9, 2, 2, 3, 4, 5, 1, 1, 1, 1])
print(qsort(l))
