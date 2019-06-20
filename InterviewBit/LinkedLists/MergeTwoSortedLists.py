"""
Merge Two Sorted Lists
======================

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists:

  5 -> 8 -> 20
  4 -> 11 -> 15
The merged list should be:

4 -> 5 -> 8 -> 11 -> 15 -> 20
"""

from __future__ import print_function
from linked_list import Node


def merge(l1, l2):
    if l1.val <= l2.val:
        head = tail = l1
        l1 = l1.next
    else:
        head = tail = l2
        l2 = l2.next

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            tail = l1
            l1 = l1.next
        else:
            tail.next = l2
            tail = l2
            l2 = l2.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return head


l1 = Node.from_iterable([5, 8, 20])
l2 = Node.from_iterable([4, 11, 15])

print(merge(l1, l2))
