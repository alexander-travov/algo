# -*- coding: utf8 -*-
"""
Commutable Islands
==================

There are A islands and there are M bridges connecting them. Each bridge has some cost attached to it.

We need to find bridges with minimal cost such that all islands are connected.

It is guaranteed that input data will contain at least one possible scenario in which all islands are connected with each other.

Input Format:

The first argument contains an integer, A, representing the number of islands.
The second argument contains an 2-d integer matrix, B, of size M x 3:
    => Island B[i][0] and B[i][1] are connected using a bridge of cost B[i][2].
Output Format:

Return an integer representing the minimal cost required.
Constraints:

1 <= A, M <= 6e4
1 <= B[i][0], B[i][1] <= A
1 <= B[i][2] <= 1e3
Examples:

Input 1:
    A = 4
    B = [   [1, 2, 1]
            [2, 3, 4]
            [1, 4, 3]
            [4, 3, 2]
            [1, 3, 10]  ]

Output 1:
    6

Explanation 1:
    We can choose bridges (1, 2, 1), (1, 4, 3) and (4, 3, 2), where the total cost incurred will be (1 + 3 + 2) = 6.

Input 2:
    A = 4
    B = [   [1, 2, 1]
            [2, 3, 2]
            [3, 4, 4]
            [1, 4, 3]   ]

Output 2:
    6

Explanation 2:
    We can choose bridges (1, 2, 1), (2, 3, 2) and (1, 4, 3), where the total cost incurred will be (1 + 2 + 3) = 6.
"""

from __future__ import print_function
from collections import namedtuple
from operator import attrgetter


Edge = namedtuple("Edge", "start stop weight")


class DSU:
    class Node:
        def __init__(self):
            self.root = None
            self.rank = 0

        def get_root(self):
            if self.root is None:
                return self
            self.root = self.root.get_root()
            return self.root

    def __init__(self, n):
        self.nodes = [DSU.Node() for _ in range(n)]

    def equivalent(self, x, y):
        return self.nodes[x-1].get_root() == self.nodes[y-1].get_root()

    def unite(self, x, y):
        xr = self.nodes[x-1].get_root()
        yr = self.nodes[y-1].get_root()
        small, big = (xr, yr) if xr.rank < yr.rank else (yr, xr)
        small.root = big
        if small.rank == big.rank:
            big.rank += 1


def kruskal(n, edges):
    dsu = DSU(n)
    edges.sort(key=attrgetter('weight'))
    mst = []
    for e in edges:
        if not dsu.equivalent(e.start, e.stop):
            dsu.unite(e.start, e.stop)
            mst.append(e)
        if len(mst) == n-1:
            break
    return mst


mst = kruskal(n=4, edges=[Edge(*e) for e in [
    [1, 2, 1],
    [2, 3, 4],
    [1, 4, 3],
    [4, 3, 2],
    [1, 3, 10]
]])
print('Cost:', sum(e.weight for e in mst))
