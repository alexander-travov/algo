"""
Magician and Chocolates
=======================

Given N bags, each bag contains Ai chocolates. There is a kid and a magician. In one unit of time, kid chooses a random bag i, eats Ai chocolates, then the magician fills the ith bag with floor(Ai/2) chocolates.

Given Ai for 1 <= i <= N, find the maximum number of chocolates kid can eat in K units of time.

For example,

K = 3
N = 2
A = 6 5

Return: 14
At t = 1 kid eats 6 chocolates from bag 0, and the bag gets filled by 3 chocolates
At t = 2 kid eats 5 chocolates from bag 1, and the bag gets filled by 2 chocolates
At t = 3 kid eats 3 chocolates from bag 0, and the bag gets filled by 1 chocolate
so, total number of chocolates eaten: 6 + 5 + 3 = 14

Note: Return your answer modulo 10^9+7

Solution
--------

Problem can be solved with a Heap data structure.

At first you heapify Ai.
Then you extract max and insert max/2 K times.

Time complexity: O(N + Klog(N)), no additional space is needed.
"""

from __future__ import print_function
from heap import MinHeap


def max_chocolates(A, K, M=int(10**9+7)):
    h = MinHeap.from_iterable((-k, k) for k in A)
    s = 0
    for _ in range(K):
        _, v = h.extract_min()
        s = (s+v) % M
        k = v//2
        h.insert(-k, k)
    return s


print(max_chocolates([6, 5], 3))
