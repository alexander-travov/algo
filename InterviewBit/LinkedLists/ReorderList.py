# -*- coding: utf8 -*-
"""
Reorder List
============

Given a singly linked list

    L: L0 → L1 → … → Ln-1 → Ln,
reorder it to:

    L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
You must do this in-place without altering the nodes’ values.
"""

from __future__ import print_function
from linked_list import Node


def reorder(l):
    break_ind = (len(l) - 1) // 2
    halves = list(l.split(break_ind))
    halves[1] = halves[1].reverse()

    head = tail = halves[0]
    halves[0] = halves[0].next
    i = 1
    while any(h is not None for h in halves):
        tail.next = halves[i]
        tail = tail.next
        halves[i] = halves[i].next
        i = 1 - i

    return head


l = Node.from_iterable([0, 1, 2, 3, 4, 5, 6])
print(reorder(l))
