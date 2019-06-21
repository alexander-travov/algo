"""
List Cycle
==========

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Solution
--------

Use Floyd's algorithm for cycle detection.
"""


from __future__ import print_function
from linked_list import Node


def cycle_start(l):
    slow = l
    fast = l.next
    if fast is None:
        return

    while fast is not slow:
        # No cycle
        if fast.next is None or fast.next.next is None:
            return
        fast = fast.next.next
        slow = slow.next

    slow = l
    fast = fast.next

    while fast is not slow:
        slow = slow.next
        fast = fast.next

    return slow


# Create linked list with cycle
l = Node.from_iterable([1, 2, 3, 4, 5])
c = Node.from_iterable([6, 7, 8, 9, 10, 11])
l.last.next = c
c.last.next = c

st = cycle_start(l)
print(st.val if st is not None else 'No cycle')
