"""
Insertion Sort List
===================

Sort a linked list using insertion sort.
"""

from __future__ import print_function
from linked_list import Node


def insertion_sort(l):
    if l is None:
        return l

    sorted_head = l
    unsorted = l.next
    l.next = None

    while unsorted is not None:
        node = sorted_head

        # insert in front of sorted list
        if unsorted.val < node.val:
            sorted_head = unsorted
            unsorted = unsorted.next
            sorted_head.next = node
        else:
            while node.next is not None and node.next.val <= unsorted.val:
                node = node.next
            sorted_tail = node.next
            node.next = unsorted
            unsorted = unsorted.next
            node.next.next = sorted_tail

    return sorted_head


l = Node.from_iterable(reversed(range(10)))
print(insertion_sort(l))
