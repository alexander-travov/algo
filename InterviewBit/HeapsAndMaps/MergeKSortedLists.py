"""
Merge K Sorted Lists
====================
Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20

Solution
--------

Use heap to effectively get next minimum element.
Time complexity O(Llog(k)) where L is the cumulative length of lists.
"""

from __future__ import print_function
from heap import MinHeap


def merge(lists):
    h = MinHeap()
    for i, l in enumerate(lists):
        # store list index and position of last element from
        # that list in min heap.
        h.insert(l[0], (i, 0))

    while h:
        min_val, (li, pos) = h.extract_min()
        yield min_val
        l = lists[li]
        pos += 1
        if pos < len(l):
            h.insert(l[pos], (li, pos))


print(list(merge((
    [1, 10, 20],
    [4, 11, 13],
    [3, 8, 9]
))))
