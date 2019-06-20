"""
Remove Duplicates from Sorted List
==================================

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

from __future__ import print_function
from linked_list import Node


def remove_duplicates(l):
    last_unique = l
    node = l.next

    while node:
        if node.val != last_unique.val:
            last_unique.next = node
            last_unique = node
        node = node.next

    last_unique.next = None

    return l


for l in (
    Node.from_iterable([1, 1, 2]),
    Node.from_iterable([1, 1, 2, 3, 3])
):
    print('Before:', l)
    print('After:', remove_duplicates(l))
