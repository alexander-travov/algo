"""
Remove Nth Node from List End
=============================

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
If n is greater than the size of the list, remove the first node of the list.
Try doing it using constant additional space.
"""

from __future__ import print_function
from linked_list import Node


def remove_nth_from_back(l, n):
    return l.remove(max(0, len(l)-n))


l = Node.from_iterable([1, 2, 3, 4, 5])
print(remove_nth_from_back(l, 2))
