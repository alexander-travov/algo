"""
Reverse Link List II
====================

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
"""

from __future__ import print_function
from linked_list import Node


def reverse(l, m, n):
    node = l
    prev = None

    for _ in range(m):
        prev = node
        node = node.next

    head_tail = prev
    rev_tail = node

    for _ in range(n-m+1):
        if not node:
            break
        next = node.next
        node.next = prev
        prev = node
        node = next

    rev_head = prev
    tail_head = node

    if head_tail is not None:
        head_tail.next = rev_head
    rev_tail.next = tail_head

    return l if m else rev_head


l = Node.from_iterable([1, 2, 3, 4, 5, 6, 7, 8])
print(reverse(l, 2, 4))
