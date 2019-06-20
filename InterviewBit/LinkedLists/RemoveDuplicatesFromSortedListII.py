"""
Remove Duplicates from Sorted List II
=====================================

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

from __future__ import print_function
from linked_list import Node


def remove_duplicates2(l):
    first_unique = last_unique = None

    node = l
    while node:
        c = 1
        # count duplicates
        while node.next and node.val == node.next.val:
            c += 1
            node = node.next

        # process uniques
        if c == 1:
            if last_unique:
                last_unique.next = node
            else:
                first_unique = node
            last_unique = node

        node = node.next

    return first_unique


for l in (
    Node.from_iterable([1, 2, 3, 4, 4, 5, 5, 6]),
    Node.from_iterable([1, 1, 2, 3, 3, 4, 5]),
    Node.from_iterable([1, 1, 2, 2, 3, 3, 3])
):
    print('Before:', l)
    print('After:', remove_duplicates2(l))
