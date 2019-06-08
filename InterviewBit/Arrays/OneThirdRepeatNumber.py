# -*- coding: utf-8 -*-
"""
N/3 Repeat Number
=================

You’re given a read only array of n integers.
Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

    Input : [1 2 3 1 1]
    Output : 1 
    1 occurs 3 times which is more than 5/3 times.


Solution
--------

The idea for the solution comes from Tetris.

Numbers "are falling" from top.
If we already have such number in bottom row then we stack new number on top of it.
If we don't have such number, we add it in the row.
If the row has 3 numbers, we destroy the row.

F.e. for sequence 3 4 3 4 5 3:

1) 3xx

2) 34x

3) 3
   34x

4) 34
   34x

5) 34  -> 34x The bottom row is destroyed
   345

6) 3
   34x

In the end the only possible candidates for numbers that occur more that n/3 times in the array should be in the bottom row.

The provided solution is generalized for any n/k proportion.

Time complexity: O(n*k), Space complexity O(k)
For k = 3:        O(n),                   O(1).
"""

from __future__ import print_function


def find_repeated_number(arr, k):
    row = [None] * k
    count = [0] * k

    for el in arr:
        if el in row:
            ind = row.index(el)
            count[ind] += 1
        elif row.count(None) > 1:
            # More that one empty spot in bottom row
            ind = row.index(None)
            row[ind] = el
            count[ind] = 1
        else:
            # Bottom row becomes full, destroing the row
            for i, c in enumerate(count):
                if c == 1:
                    row[i] = None
                count[i] = max(0, count[i]-1)

    for el in row:
        if arr.count(el) > len(arr)/float(k):
            yield el


arr = [2, 2, 3, 1, 1, 2, 1, 2]
print(arr, list(find_repeated_number(arr, 3)))
