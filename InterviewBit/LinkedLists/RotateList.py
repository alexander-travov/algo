"""
Rotate List
===========

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:

Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

from __future__ import print_function
from linked_list import Node


def rotate(l, k):
    n = len(l)
    k %= n
    if k == 0:
        return l
    prev = l.nth(n-k-1)
    head = prev.next
    prev.next = None
    head.last.next = l
    return head


l = Node.from_iterable([1, 2, 3, 4, 5])
print(rotate(l, 22))
