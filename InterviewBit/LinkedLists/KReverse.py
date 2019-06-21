# -*- coding: utf8 -*-
"""
K reverse linked list
=====================

Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

 NOTE : The length of the list is divisible by K
Example :

Given linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6 and K=2,

You should return 2 -> 1 -> 4 -> 3 -> 6 -> 5

Try to solve the problem using constant extra space.
"""

from __future__ import print_function
from linked_list import Node


def kreverse(l, k):
    heads = [None] * k
    tails = [None] * k

    node = l
    i = 0
    while node:
        if heads[i] is None:
            heads[i] = node
        if tails[i] is not None:
            tails[i].next = node
        tails[i] = node
        node = node.next
        tails[i].next = None
        i = (i+1) % k

    out_head = out_tail = None
    i = k-1
    while any(h is not None for h in heads):
        if heads[i] is not None:
            if out_head is None:
                out_head = heads[i]
            if out_tail is not None:
                out_tail.next = heads[i]
            out_tail = heads[i]
            heads[i] = heads[i].next
            out_tail.next = None
        i = (i-1) % k
    
    return out_head


l = Node.from_iterable(range(10))
print(kreverse(l, 3))
