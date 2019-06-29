"""
Ways to form Max Heap
=====================

How many distinct Max Heap can be made from n distinct integers

Solution
--------

heap of height h can have from 2^h to 2^(h+1)-1 nodes

So if a heap has n nodes it is of height floor(log2(n))
"""

from __future__ import print_function
from math import log


def C(n, k):
    k = min(k, n-k)
    if k == 0:
        return n
    res = 1
    for i in range(k):
        res *= n-i
    for i in range(k):
        res //= i+1
    return res


NUM_WAYS = {0:1, 1:1}
def num_heaps(n):
    if n in NUM_WAYS:
        return NUM_WAYS[n]
    h = int(log(n, 2))
    l_nodes = r_nodes = 2**(h-1)-1
    num_leafs = n - 1 - 2*l_nodes
    l_leafs = min(2**(h-1), num_leafs)
    r_leafs = num_leafs - l_leafs
    l_nodes += l_leafs
    r_nodes += r_leafs
    res = C(n-1, r_nodes) * num_heaps(l_nodes) * num_heaps(r_nodes)
    NUM_WAYS[n] = res
    return res


for i in range(18):
    print(i, num_heaps(i))
