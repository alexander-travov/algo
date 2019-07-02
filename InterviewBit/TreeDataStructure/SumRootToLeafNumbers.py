"""
Sum Root to Leaf Numbers
========================

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers % 1003.

Example :

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = (12 + 13) % 1003 = 25 % 1003 = 25.
"""

from __future__ import print_function
from itertools import chain


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def numbers(node):
    # Leaf node
    if node.left is None and node.right is None:
        yield (node.data, 0)
    for n, d in chain(
            numbers(node.left) if node.left else [],
            numbers(node.right) if node.right else []
        ):
        yield (node.data * 10**(d+1) + n, d+1)


tree = Node(5, Node(4), Node(3, Node(2), Node(1)))
print(sum(n[0] for n in numbers(tree)))
