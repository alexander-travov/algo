"""
Min XOR value
=============

Given an array of N integers, find the pair of integers in the array which have minimum XOR value.
Report the minimum XOR value.

Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000

Solution
--------

1. We can build trie for "words" consisting of 32 bits for every number.

As we add words to the trie, we keep:
- the maximum height from root at which occured the last node split.
- the minimum XOR value of 2 "word" endings that start at that node.


We can see, that if such split occurs nearer to the root, the resulting XOR value would be greater.

Time complexity: O(n), extra space O(n).

2. As we see from the trie solution, min XOR is guaranteed to be between the adjacent numbers if they are sorted.
So we can sort array and find min XOR with linear search.

Time complexity: O(n log(n)), extra space O(1).
"""

from __future__ import print_function
import sys


class Node:
    def __init__(self):
        self.children = [None, None]

    def value(self, order='min'):
        """
        Reads value of min/max integer stored in trie from this node.
        """
        # order in which child nodes are traversed
        bits = (0, 1) if order=='min' else (1, 0)

        node = self
        v = 0
        while True:
            ch = node.children
            # Leaf
            if not any(ch):
                break
            for b in bits:
                if ch[b]:
                    break
            node = ch[b]
            v <<= 1
            v += b
        return v

    def xor(self):
        """
        Gets XOR value of min and max numbers stored from this node.
        """
        return self.value('min') ^ self.value('max')


class MinXORTrie:
    def __init__(self):
        self.root = Node()
        self.min_xor = sys.maxsize

    def insert(self, n):
        node = self.root
        split_node = None

        for i in range(31, -1, -1):
            bit = (n>>i) & 1
            if node.children[bit] is None:
                # Save the first nonexistent split
                if split_node is None:
                    split_node = node
                node.children[bit] = Node()
            node = node.children[bit]

        if split_node and all(split_node.children):
            self.min_xor = min(self.min_xor, split_node.xor())


t = MinXORTrie()
arr = [0, 4, 7, 9, 2, 1]
for n in arr:
    t.insert(n)
    print(n, t.min_xor)
print(t.min_xor)
