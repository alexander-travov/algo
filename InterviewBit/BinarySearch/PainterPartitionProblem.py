"""
Painter's Partition Problem
===========================

You have to paint N boards of length {A0, A1, A2, A3 … AN-1}.
There are K painters available and you are also given how much time a painter takes to paint 1 unit of board.
You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.

A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.

Return the ans % 10000003.

Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board

Output:
return minimum time to paint all boards % 10000003

Example
-------

Input : 
  K : 2
  T : 5
  L : [1, 10]
Output : 50

Solution
--------

0. Find S=sum(arr)
1. Then binary search between 1 and S for the first integer I such that there exists a division of array
in K consecutive chunks such that the sum in each chunk is less that I.
2. I*T is the answer

Time complexity: O(N*log(S))
"""

from __future__ import print_function


def partition_possible(boards, k, max_len):
    s = 0
    num_chunks = 1
    for i, el in enumerate(boards):
        if el > max_len:
            return False
        s += el
        if s > max_len:
            num_chunks += 1
            if num_chunks > k:
                return False
            s = el
    return True
            

def find_min_paint_time(boards, k, t, m=10000003):
    low = 1
    high = sum(boards)
    res = -1
 
    while low <= high:
        mid = low + (high-low)//2
        if partition_possible(boards, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    if res > 0:
        return res*t % m
    return -1


print(find_min_paint_time([1, 1, 2, 1, 7, 10, 1, 3, 8, 1], 4, 5))
