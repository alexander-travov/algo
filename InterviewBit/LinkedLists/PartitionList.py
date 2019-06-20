"""
Partition List
==============

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

from __future__ import print_function
from linked_list import Node


def partition(l, x):
    heads = [None, None]
    tails = [None, None]

    while l:
        ind = int(l.val >= x)
        if heads[ind] is None:
            heads[ind] = l
        if tails[ind] is not None:
            tails[ind].next = l
        tails[ind] = l
        l = l.next
        tails[ind].next = None

    if tails[0]:
        tails[0].next = heads[1]
    return heads[0] or heads[1]


l = Node.from_iterable([1, 4, 3, 2, 5, 2])
print(partition(l, 3))
