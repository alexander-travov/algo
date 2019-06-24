"""
Combinations
============

Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
"""

from __future__ import print_function


def combinations(n, k, min_n=1):
    if k == 0:
        yield []
    elif n+1-min_n == k:
        yield list(range(min_n, n+1))
    else:
        for c in combinations(n, k-1, min_n+1):
            yield [min_n] + c
        for c in combinations(n, k, min_n+1):
            yield c


for c in combinations(5, 3):
    print(c)
